import asyncio
from dataclasses import asdict
import json
import random
import sys

from pywsp import (
    WebSocket, WebSocketCallback, WebSocketClient, WebSocketMessage
)

from aiohttp.client_exceptions import (
    ClientConnectorError, ServerDisconnectedError
)

sys.path += ".."
from src import jsonutils
from src.websocketmessages import *

class Program(WebSocketCallback):
    def __init__(self):
        self.client = WebSocketClient(message_factory)
        self.client.register_callback(self)
        self.msgid = 1
        self.ws = None

    def send_status_request(self, thermostats):
        request = StatusRequestMessage(self.msgid, thermostats)
        self.msgid += 1
        print(f"Sending message: {request}")
        asyncio.create_task(self.ws.send_message(request))

    def on_new_connection(self, ws: WebSocket) -> None:
        self.ws = ws
        print(f"Connected to {ws.peer_info.ip}:{ws.peer_info.port}")
        self.send_status_request([])

    async def on_new_message(self, ws: WebSocket, message: WebSocketMessage) -> None:
        print(f"Received message: {message}")
        print(f"=> {json.dumps(asdict(message), indent=2)}")
        if isinstance(message, EventMessage):
            if message.name == "thermostat_updated":
                self.send_status_request(message.args["thermostats"])

    async def run(self):
        url = "http://192.168.1.182:8787/api/websocket"
        while True:
            try:
                await self.client.run(url)
            except ServerDisconnectedError:
                print(f"Server disconnected. Retrying...")
                await asyncio.sleep(3)
            except ClientConnectorError:
                print(f"Could not connect to server. Retrying...")
                await asyncio.sleep(3)
            except Exception as e:
                print(f"Unknown error {e}. Retrying...")
                await asyncio.sleep(3)

if __name__ == "__main__":
    random.seed()
    program = Program()
    try:
        asyncio.run(program.run())
    except KeyboardInterrupt:
        pass
