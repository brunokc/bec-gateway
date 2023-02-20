from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
import random

from aiohttp import web, WSMsgType
from aiohttp.web import Request, StreamResponse
from typing import Any, List, Optional, Tuple

from . import jsonutils

_LOGGER = logging.getLogger(__name__)

@dataclass
class WebSocketMessage:
    id: int
    action: str
    args: Optional[List[str]] = None
    response: Optional[dict[str, Any]] = None

    def __str__(self):
        str = {
            "id": self.id,
            "action": self.action,
        }
        if self.args is not None:
            str["args"] = self.args
        if self.response is not None:
            str["response"] = self.response
        return jsonutils.dumps(str)


class WebSocketServerCallback(ABC):
    @abstractmethod
    def on_new_connection(self, ws: web.WebSocketResponse, client_ip: str, client_port: int):
        pass

    @abstractmethod
    async def on_new_message(self, ws: web.WebSocketResponse, client_ip: str, client_port: int, message: WebSocketMessage):
        pass


class WebSocketServer:
    def __init__(self, address: str, port: int):
        self._address = address
        self._port = port
        self._callback: WebSocketServerCallback
        random.seed()

    def register_callback(self, callback: WebSocketServerCallback) -> None:
        self._callback = callback

    async def handle_binary(self, data: bytes) -> None:
        _LOGGER.debug("received binary payload")
        _LOGGER.debug(data)

    def get_peer_info(self, request: Request) -> Tuple[str, int]:
        client_ip = ""
        client_port = 0
        peername = None
        if request.transport:
            peername = request.transport.get_extra_info("peername")
        if peername is not None:
            client_ip, client_port = peername
        return client_ip, client_port

    async def wshandler(self, request: Request) -> StreamResponse:
        if self._callback is None:
            _LOGGER.debug("ignoring connection due to empty callback")
            return None

        client_ip, client_port = self.get_peer_info(request)
        _LOGGER.debug(f"connection from %s:%d", client_ip, client_port)

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        self._callback.on_new_connection(ws, client_ip, client_port)

        async for msg in ws:
            _LOGGER.debug("new message %s", msg.__repr__())

            if msg.type == WSMsgType.TEXT:
                if msg.data == "close":
                    await ws.close()
                else:
                    await self.dispatch_callback(ws, client_ip, client_port, msg.json())
            elif msg.type == WSMsgType.BINARY:
                await self.dispatch_callback(ws, client_ip, client_port, msg.data)
            elif msg.type == WSMsgType.ERROR:
                _LOGGER.debug("error %s", ws.exception())

        _LOGGER.debug("connection closed")

    async def dispatch_callback(self, ws, client_ip, client_port, data):
        if "id" not in data:
            _LOGGER.error("message doesn't contain an id. Discarding...")
            return
        if "action" not in data:
            _LOGGER.error("message doesn't contain a action. Discarding...")
            return

        message = WebSocketMessage(data["id"], data["action"],
            data["args"] if "args" in data else None)
        await self._callback.on_new_message(ws, client_ip, client_port, message)

    async def send_response(self, ws, msg: WebSocketMessage, data):
        message = WebSocketMessage(msg.id, msg.action, response=data)
        await ws.send_json(message, dumps=jsonutils.dumps)

    async def run(self) -> None:
        app = web.Application()
        # app.add_routes([web.get("/api/ws", self.wshandler)])
        app.router.add_get("/api/ws", self.wshandler)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._address, self._port)
        await site.start()
        _LOGGER.debug("serving on %s:%d", self._address, self._port)
