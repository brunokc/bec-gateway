import asyncio
import logging
from typing import Any, Dict

from .handlermaps import ProcessingResult
from .requesthandler import ConnexRequestHandler
from .thermostat import ConnexThermostat
from .websocket import WebSocketMessage, WebSocketServer, WebSocketServerCallback

from . import jsonutils

_LOGGER = logging.getLogger(__name__)

class Service(WebSocketServerCallback):
    def __init__(self, proxy_ip: str, proxy_port: int, ws_ip: str, ws_port: int):
        self._has_updates = False
        self.thermostats: Dict[str, ConnexThermostat] = { }

        self.handler = ConnexRequestHandler(proxy_ip, proxy_port)
        self.handler.register_callback(self.update_thermostat)

        self.websocket = WebSocketServer(ws_ip, ws_port)
        self.websocket.register_callback(self)

        self._ws_action_map = {
            "getStatus": self.ws_get_status
        }


    def update_thermostat(self, result: ProcessingResult) -> None:
        serial_number = result.keys["serial_number"]
        if serial_number not in self.thermostats:
            self.thermostats[serial_number] = ConnexThermostat(serial_number)

        thermostat = self.thermostats[serial_number]
        thermostat.update(result.type, result.dataset)
        self._has_updates = True


    def on_new_connection(self, ws, client_ip: str, client_port: int) -> None:
        _LOGGER.debug("New websocket client connected: (%s:%s)", client_ip, client_port)


    async def ws_get_status(self, ws, message):
        result = { }
        thermostats = []
        for t in self.thermostats.values():
            thermostats.append({
                "serial_number": t.serial_number,
                "lastUpdated": t.status.lastUpdated,
                "status": t.status.data
            })

        result["thermostats"] = thermostats
        await self.websocket.send_response(ws, message, result)


    async def on_new_message(self, ws, client_ip: str, client_port: int, message: WebSocketMessage) -> None:
        _LOGGER.debug("new websocket message (%s:%s): %s", client_ip, client_port, jsonutils.dumps(message))
        if message.action in self._ws_action_map:
            handler = self._ws_action_map[message.action]
            await handler(ws, message)


    async def run(self) -> None:
        # await asyncio.gather(self.handler.run(), self.websocket.run())
        pending = [self.handler.run(), self.websocket.run()]
        while True:
            __, pending = await asyncio.wait(pending, timeout=5)
            if self.thermostats and self._has_updates:
                self._has_updates = False
                _LOGGER.debug("Thermostats:")
                for t in self.thermostats.values():
                    _LOGGER.debug("Serial Number: %s", t.serial_number)
                    _LOGGER.debug("Status (%s): %s", t.status.lastUpdated, t.status)
                    _LOGGER.debug("Ping rates/Changes Pending: %s", t.ping_rates)
                    _LOGGER.debug("IDU Status (%s): %s", t.idustatus.lastUpdated, t.idustatus)
                    _LOGGER.debug("ODU Status (%s): %s", t.odustatus.lastUpdated, t.odustatus)
