from abc import ABC, abstractmethod
import logging
import random
import sys

from aiohttp import web, WSMsgType
from aiohttp.web import Request, StreamResponse
from typing import List, NamedTuple, Optional, Tuple

from . import jsonutils

_LOGGER = logging.getLogger(__name__)

class WebSocketCommand(NamedTuple):
    id: int
    command: str
    args: Optional[List[str]]


class WebSocketServerCallback(ABC):
    @abstractmethod
    def on_new_connection(self, ws: web.WebSocketResponse, client_ip: str, client_port: int):
        pass

    @abstractmethod
    async def on_new_message(self, ws: web.WebSocketResponse, client_ip: str, client_port: int, message: WebSocketCommand):
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
        if "command" not in data:
            _LOGGER.error("message doesn't contain a command. Discarding...")
            return

        command = WebSocketCommand(data["id"], data["command"],
            data["args"] if "args" in data else None)
        await self._callback.on_new_message(ws, client_ip, client_port, command)

    async def send_response(self, ws, command: WebSocketCommand, data):
        response = {
            "id": command.id,
            "command": command.command,
            "response": data
        }
        await ws.send_json(response, dumps=jsonutils.dumps)

    async def run(self) -> None:
        app = web.Application()
        # app.add_routes([web.get("/api/ws", self.wshandler)])
        app.router.add_get("/api/ws", self.wshandler)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._address, self._port)
        await site.start()
        _LOGGER.debug("serving on %s:%d", self._address, self._port)
