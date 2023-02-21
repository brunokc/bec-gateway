import asyncio
import aiohttp
import json
import random
import sys

sys.path += ".."
from src import jsonutils

async def call(ws, command, args=None):
    message = {
        "id": random.randint(1, sys.maxsize),
        "action": command,
    }
    if args is not None:
        message["args"] = args

    print(f"Sending: {jsonutils.dumps(message)}")
    await ws.send_json(message)


async def get_status(ws, args=None):
    await call(ws, "getStatus", args)


async def dispatch(ws, msg):
    id = msg["id"]
    action = msg["action"]
    args = msg["args"] if "args" in msg else None
    response = msg["response"] if "response" in msg else None

    print(f"Server (raw): {msg}")
    print(f"WebSocketMessage: id={id}; action={action}")
    if args is not None:
        print(f"  args: {jsonutils.dumps(args, indent=2)}")
    if response is not None:
        print(f"  response: {jsonutils.dumps(response, indent=2)}")

    if (action == "raiseEvent" and args is not None and args["event"] == "thermostatUpdated"
        and "payload" in args):

        thermostats = args["payload"]["thermostats"]
        await get_status(ws, thermostats)

    # data = json.loads(msg.data)
    # print(f"Server (json): {jsonutils.dumps(data, indent=2)}")


async def run():
    async with aiohttp.ClientSession() as session:
        url = "http://192.168.1.182:8787/api/ws"
        async with session.ws_connect(url) as ws:
            while True:
                print(f"Connected to {url}")
                command_task = asyncio.create_task(get_status(ws))

                print("Waiting for messages...")
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        data = msg.data
                        if data == 'close cmd':
                            await ws.close()
                            break
                        else:
                            # print(f"data({type(data)})={data}")
                            jsondata = json.loads(data)
                            # print(f"jsondata({type(jsondata)})={jsondata}")
                            await dispatch(ws, jsondata)
                    elif msg.type == aiohttp.WSMsgType.BINARY:
                        #self.handle_request(msg.data)
                        pass
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        break


if __name__ == "__main__":
    random.seed()
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass