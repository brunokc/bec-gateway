import asyncio
from datetime import datetime, timezone
import logging
from pywsp import (
    WebSocket, WebSocketMessage, WebSocketServer, WebSocketCallback
)
from typing import Any, Dict, List, Optional, Set

from .handlermaps import ProcessingResult
from .requesthandler import ConnexRequestHandler
from .thermostat import ConnexThermostat
from .websocketmessages import *

from . import jsonutils

_LOGGER = logging.getLogger(__name__)

class Service(WebSocketCallback):
    def __init__(self, proxy_ip: str, proxy_port: int, ws_ip: str, ws_port: int, ws_url: str):
        self._has_updates = False
        self.lastUpdated = datetime.min
        self.thermostats: Dict[str, ConnexThermostat] = { }
        self._ws_ip = ws_ip
        self._ws_port = ws_port
        self._ws_url = ws_url

        self.handler = ConnexRequestHandler(proxy_ip, proxy_port)
        self.handler.register_callback(self.update_thermostat)

        self.wsserver = WebSocketServer(message_factory)
        self.wsserver.register_callback(self)
        self._websocket: Optional[WebSocket] = None

        self._ws_action_map = {
            "getStatus": self.ws_get_status
        }

        self._ws_message_type_map = {
            StatusRequestMessage: self._ws_status_request
        }


    def update_thermostat(self, result: ProcessingResult) -> None:
        serial_number = result.keys["serial_number"]
        if serial_number not in self.thermostats:
            self.thermostats[serial_number] = ConnexThermostat(serial_number)

        thermostat = self.thermostats[serial_number]
        thermostat.update(result.type, result.dataset)
        self._has_updates = True
        self.lastUpdated = datetime.now(timezone.utc)
        asyncio.create_task(self.raise_update_event(serial_number))


    def on_new_connection(self, ws: WebSocket) -> None:
        _LOGGER.debug("new websocket client connected: (%s:%s)",
            ws.peer_info.ip, ws.peer_info.port)
        self._websocket = ws


    async def ws_get_status(self, ws: WebSocket, message: WebSocketMessage) -> None:
        serial_numbers = None
        if message.args is not None:
            args = message.args
            assert isinstance(args, list) or isinstance(args, str)
            if isinstance(args, list):
                serial_numbers = [x for x in args]
            elif isinstance(args, str):
                serial_numbers = [args]

        result: Dict[str, Any] = { }
        thermostats: List[Dict[str, Any]] = []
        for t in self.thermostats.values():
            if serial_numbers is not None:
                if t.serial_number not in serial_numbers:
                    continue

            thermostats.append({
                "serial_number": t.serial_number,
                "lastUpdated": t.status.lastUpdated,
                "status": t.status.data
            })

        result["lastUpdated"] = self.lastUpdated
        result["thermostats"] = thermostats
        await ws.send_response(message, result)

    async def _ws_status_request(self, ws: WebSocket, message: StatusRequestMessage) -> None:
        serial_numbers = message.args

        thermostats: List[Thermostat] = []
        for t in self.thermostats.values():
            if serial_numbers and t.serial_number not in serial_numbers:
                continue

            thermostats.append(Thermostat(
                serial_number=t.serial_number,
                last_updated=t.status.lastUpdated.isoformat(),
                status=t.status.data
            ))

        response = StatusResponseMessage(
            id=message.id,
            last_updated=jsonutils.to_iso_format(self.lastUpdated),
            thermostats=thermostats
        )
        await ws.send_message(response)


    async def on_new_message(self, ws: WebSocket, message: WebSocketMessage) -> None:
        _LOGGER.debug("new websocket message (%s:%s): %s", ws.peer_info.ip, ws.peer_info.port, jsonutils.dumps(message))
        # if message.action in self._ws_action_map:
        #     handler = self._ws_action_map[message.action]
        #     await handler(ws, message)
        handler = self._ws_message_type_map.get(type(message), None)
        if handler is not None:
            await handler(ws, message)


    async def raise_update_event(self, serial_number: str) -> None:
        if self._websocket:
            event = EventMessage(0, "thermostat_updated", { "thermostats": [serial_number] })

            try:
                await self._websocket.send_message(event)
            except ConnectionResetError:
                _LOGGER.debug("websocket connection lost")
                self._websocket = None


    async def run(self) -> None:
        # await asyncio.gather(self.handler.run(), self.wsserver.run())
        pending: Set[asyncio.Task[None]] = {
            asyncio.create_task(self.handler.run()),
            asyncio.create_task(self.wsserver.run(self._ws_ip, self._ws_port, self._ws_url))
        }
        while True:
            __, pending = await asyncio.wait(pending, timeout=5)
            if self.thermostats and self._has_updates:
                self._has_updates = False
                _LOGGER.debug("Thermostats:")
                for t in self.thermostats.values():
                    _LOGGER.debug("Serial Number: %s", t.serial_number)
                    _LOGGER.debug("Status (%s): %s", t.status.lastUpdated.isoformat(), t.status)
                    _LOGGER.debug("Ping rates/Changes Pending: %s", t.ping_rates)
                    _LOGGER.debug("IDU Status (%s): %s", t.idustatus.lastUpdated.isoformat(), t.idustatus)
                    _LOGGER.debug("ODU Status (%s): %s", t.odustatus.lastUpdated.isoformat(), t.odustatus)
