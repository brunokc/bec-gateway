import asyncio
from dataclasses import asdict
# import aiohttp
import json
import random
import sys

from pywsp import WebSocket, WebSocketCallback, WebSocketClient, WebSocketMessage

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


    # async def call(self, ws, command, args=None):
    #     message = {
    #         "id": random.randint(1, sys.maxsize),
    #         "action": command,
    #     }
    #     if args is not None:
    #         message["args"] = args

    #     print(f"Sending: {jsonutils.dumps(message)}")
    #     await ws.send_json(message)


    # async def get_status(self, ws, args=None):
    #     await self.call(ws, "getStatus", args)


    # async def dispatch(self, ws, msg):
    #     id = msg["id"]
    #     action = msg["action"]
    #     args = msg["args"] if "args" in msg else None
    #     response = msg["response"] if "response" in msg else None

    #     print(f"Server (raw): {msg}")
    #     print(f"WebSocketMessage: id={id}; action={action}")
    #     if args is not None:
    #         print(f"  args: {jsonutils.dumps(args, indent=2)}")
    #     if response is not None:
    #         print(f"  response: {jsonutils.dumps(response, indent=2)}")

    #     if (action == "raiseEvent" and args is not None and args["event"] == "thermostatUpdated"
    #         and "payload" in args):

    #         thermostats = args["payload"]["thermostats"]
    #         await self.get_status(ws, thermostats)

    #     # data = json.loads(msg.data)
    #     # print(f"Server (json): {jsonutils.dumps(data, indent=2)}")


    # async def handle_connection(self, ws):
    #     command_task = asyncio.create_task(self.get_status(ws))

    #     print("Waiting for messages...")
    #     async for msg in ws:
    #         if msg.type == aiohttp.WSMsgType.TEXT:
    #             data = msg.data
    #             if data == 'close cmd':
    #                 await ws.close()
    #                 break
    #             else:
    #                 # print(f"data({type(data)})={data}")
    #                 jsondata = json.loads(data)
    #                 # print(f"jsondata({type(jsondata)})={jsondata}")
    #                 await dispatch(ws, jsondata)
    #         elif msg.type == aiohttp.WSMsgType.BINARY:
    #             #self.handle_request(msg.data)
    #             pass
    #         elif msg.type == aiohttp.WSMsgType.ERROR:
    #             break


    async def run(self):
        url = "http://192.168.1.182:8787/api/websocket"
        while True:
            try:
                # async with session.ws_connect(url) as ws:
                await self.client.run(url)
                # print(f"Connected to {url}")
                # await handle_connection(ws)
            except ServerDisconnectedError:
                print(f"Server disconnected. Retrying...")
                await asyncio.sleep(3)
            except ClientConnectorError:
                print(f"Could not connect to server. Retrying...")
                await asyncio.sleep(3)


if __name__ == "__main__":
    random.seed()
    program = Program()
    try:
        asyncio.run(program.run())
    except KeyboardInterrupt:
        pass
