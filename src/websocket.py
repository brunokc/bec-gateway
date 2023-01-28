import json
import logging

from aiohttp import web, WSMsgType
from aiohttp.web import Request, StreamResponse
from typing import Awaitable, Callable, Union, Tuple

_LOGGER = logging.getLogger(__name__)

CallbackType = Callable[[str, int, str], Awaitable[None]]

class WebSocketServer:
    def __init__(self, address: str, port: int):
        self._address = address
        self._port = port
        self._callback: CallbackType

    def register_callback(self, callback: CallbackType) -> None:
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
        client_ip, client_port = self.get_peer_info(request)
        _LOGGER.debug(f"connection from %s:%d", client_ip, client_port)

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            _LOGGER.debug("new message %s", msg.__repr__())

            if self._callback is None:
                _LOGGER.debug("ignoring message due to empty callback")
                continue

            if msg.type == WSMsgType.TEXT:
                if msg.data == "close":
                    await ws.close()
                else:
                    await self._callback(client_ip, client_port, msg.data)
            elif msg.type == WSMsgType.BINARY:
                await self._callback(client_ip, client_port, msg.data)
            elif msg.type == WSMsgType.ERROR:
                _LOGGER.debug("connection closed with exception %s", ws.exception())

        _LOGGER.debug("connection closed")

    async def run(self) -> None:
        app = web.Application()
        # app.add_routes([web.get("/api/ws", self.wshandler)])
        app.router.add_get("/api/ws", self.wshandler)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._address, self._port)
        await site.start()
        _LOGGER.debug("serving on %s:%d", self._address, self._port)
