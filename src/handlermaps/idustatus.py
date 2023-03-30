from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import Map
from . import util
from . import BaseHandler, DataSetType, ProcessingResult

# POST /systems/1117W005762/idu_status
# <idu_status version="1.7">
#     <idutype>furnace2stg</idutype>
#     <pwmblower>off</pwmblower>
#     <opstat>off</opstat>
#     <iducfm>0</iducfm>
#     <blwrpm>0</blwrpm>
#     <statpress>0.00</statpress>
#     <coiltemp>na</coiltemp>
#     <inducerrpm>na</inducerrpm>
#     <lat>na</lat>
#     <lockoutactive>off</lockoutactive>
#     <lockouttime>off</lockouttime>
# </idu_status>

# IDU (InDoor Unit) Status handler map
request_map: Map = {
    "/idu_status/idutype": {
        "name": "indoorUnitType",
        "handler": util.tostr
    },
    "/idu_status/pwmblower": {
        "name": "?pwmBlower",
        "handler": util.tostr
    },
    "/idu_status/opstat": {
        "name": "?opstat",
        "handler": util.tostr
    },
    "/idu_status/iducfm": {
        "name": "indoorUnitCFM",
        "handler": util.toint
    },
    "/idu_status/blwrpm": {
        "name": "blowerRPM",
        "handler": util.toint
    },
    "/idu_status/statpress": {
        "name": "staticPressure",
        "handler": util.tofloat
    },
    "/idu_status/coiltemp": {
        "name": "coilTemperature",
        "handler": util.toint
    },
}

class IduStatusHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/idu_status"
        self.type = DataSetType.IduStatus
        self.request_map = request_map
        self.response_map = { }

    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        dataset = await self.process_form_data(request)
        keys = { "serial_number": matches[0] }
        return ProcessingResult(self.type, keys, dataset)

    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        return ProcessingResult.Empty
