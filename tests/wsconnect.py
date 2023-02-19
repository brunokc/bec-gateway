import asyncio
import aiohttp
import json
import random
import sys

async def call(ws, command, args=None):
    message = {
        "id": random.randint(1, sys.maxsize),
        "command": command,
    }
    if args is not None:
        message["args"] = args

    await ws.send_json(message)


async def get_status(ws):
    while True:
        await call(ws, "getStatus")
        await asyncio.sleep(10)


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
                        if msg.data == 'close cmd':
                            await ws.close()
                            break
                        else:
                            data = json.loads(msg.data)
                            print(f"Server: {json.dumps(data, indent=2)}")
                    elif msg.type == aiohttp.WSMsgType.BINARY:
                        #self.handle_request(msg.data)
                        pass
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        break


if __name__ == "__main__":
    random.seed()
    asyncio.run(run())
