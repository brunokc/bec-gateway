import asyncio
from typing import Dict

from .handlermaps import ProcessingResult
from .requesthandler import ConnexRequestHandler
from .thermostat import ConnexThermostat
from .websocket import WebSocketServer

class Service:
    def __init__(self, proxy_ip: str, proxy_port: int, ws_ip: str, ws_port: int):
        self._has_updates = False
        self.thermostats: Dict[str, ConnexThermostat] = { }

        self.handler = ConnexRequestHandler(proxy_ip, proxy_port)
        self.handler.register_callback(self.update_thermostat)

        self.websocket = WebSocketServer(ws_ip, ws_port)
        self.websocket.register_callback(self.on_new_message)


    def update_thermostat(self, result: ProcessingResult) -> None:
        serial_number = result.keys["serial_number"]
        if serial_number not in self.thermostats:
            self.thermostats[serial_number] = ConnexThermostat(serial_number)

        thermostat = self.thermostats[serial_number]
        thermostat.update(result.type, result.dataset)
        self._has_updates = True


    async def on_new_message(self, client_ip: str, client_port: int, data: str) -> None:
        pass


    async def run(self) -> None:
        # await asyncio.gather(self.handler.run(), self.websocket.run())
        pending = [self.handler.run(), self.websocket.run()]
        while True:
            done, pending = await asyncio.wait(pending, timeout=5)
            if self.thermostats and self._has_updates:
                self._has_updates = False
                print("Thermostats:")
                for t in self.thermostats.values():
                    print(f"Serial Number: {t.serial_number}")
                    print(f"Status ({t.status.lastUpdated}): {t.status}")
                    print(f"Ping rates/Changes Pending: {t.ping_rates}")
                    print(f"IDU Status ({t.idustatus.lastUpdated}): {t.idustatus}")
                    print(f"ODU Status ({t.odustatus.lastUpdated}): {t.odustatus}")
