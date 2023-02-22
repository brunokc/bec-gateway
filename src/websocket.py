from abc import ABC, abstractmethod
from dataclasses import dataclass
import logging
import random

from aiohttp import web, WSMsgType
from aiohttp.web import Request, StreamResponse
from typing import Any, Dict, List, Optional, Tuple, Union

from . import jsonutils

_LOGGER = logging.getLogger(__name__)

@dataclass
class WebSocketMessage:
    id: int
    action: str
    args: Optional[Union[str, List[str], dict[str, Any]]] = None
    response: Optional[dict[str, Any]] = None

    def __str__(self) -> str:
        str = {
            "id": self.id,
            "action": self.action,
        }
        if self.args is not None:
            str["args"] = self.args
        if self.response is not None:
            str["response"] = self.response
        return jsonutils.dumps(str)


class WebSocket:
    def __init__(self, client_ip: str, client_port: int, callback: "WebSocketServerCallback") -> None:
        self._ws = web.WebSocketResponse()
        self.client_ip = client_ip
        self.client_port = client_port
        self._callback = callback

    async def send_response(self, msg: WebSocketMessage, data: dict[str, Any]) -> None:
        message = WebSocketMessage(msg.id, msg.action, response=data)
        await self._ws.send_str(str(message))

    async def send_message(self, message: WebSocketMessage) -> None:
        await self._ws.send_str(str(message))

    async def handle_messages(self, request: Request) -> None:
        await self._ws.prepare(request)

        self._callback.on_new_connection(self)

        async for msg in self._ws:
            _LOGGER.debug("new message %s", msg.__repr__())

            if msg.type == WSMsgType.TEXT:
                if msg.data == "close":
                    await self._ws.close()
                else:
                    await self.dispatch_callback(msg.json())
            elif msg.type == WSMsgType.BINARY:
                await self.dispatch_callback(msg.data)
            elif msg.type == WSMsgType.ERROR:
                _LOGGER.debug("error %s", self._ws.exception())

    async def dispatch_callback(self, data: Dict[str, Any]) -> None:
        if "id" not in data:
            _LOGGER.error("message doesn't contain an id. Discarding...")
            return
        if "action" not in data:
            _LOGGER.error("message doesn't contain an action. Discarding...")
            return

        message = WebSocketMessage(data["id"], data["action"],
            data["args"] if "args" in data else None)
        await self._callback.on_new_message(self, message)

    async def raise_event(self, event: str, payload: Dict[str, Any]) -> None:
        args = {
            "event": event,
            "payload": payload
        }
        message = WebSocketMessage(0, "raiseEvent", args=args)
        await self.send_message(message)


class WebSocketServerCallback(ABC):
    @abstractmethod
    def on_new_connection(self, ws: WebSocket) -> None:
        pass

    @abstractmethod
    async def on_new_message(self, ws: WebSocket, message: WebSocketMessage) -> None:
        pass


class WebSocketServer:
    def __init__(self, address: str, port: int):
        self._address = address
        self._port = port
        self._callback: WebSocketServerCallback
        random.seed()
        self.clients: List[WebSocket] = []

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
        assert self._callback is not None

        client_ip, client_port = self.get_peer_info(request)
        _LOGGER.debug(f"connection from %s:%d", client_ip, client_port)

        ws = WebSocket(client_ip, client_port, self._callback)

        self.clients.append(ws)
        try:
            await ws.handle_messages(request)
        finally:
            self.clients.remove(ws)

        _LOGGER.debug("connection closed")
        return ws._ws

    async def raise_event(self, event: str, args: Dict[str, Any]) -> None:
        for client in self.clients:
            await client.raise_event(event, args)

    async def run(self) -> None:
        if self._callback is None:
            _LOGGER.debug("No callback defined, canceling websocket")
            raise RuntimeError("Starting websocket without setting a callback")

        app = web.Application()
        app.router.add_get("/api/ws", self.wshandler)

        runner = web.AppRunner(app)
        await runner.setup()
        site = web.TCPSite(runner, self._address, self._port)
        await site.start()
        _LOGGER.debug("serving on %s:%d", self._address, self._port)
