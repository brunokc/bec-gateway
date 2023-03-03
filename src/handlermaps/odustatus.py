from pyproxy.httprequest import HttpRequest, HttpResponse
from typing import List

from . import Map
from . import util
from . import BaseHandler, DataSetType, ProcessingResult

# POST /systems/1117W005762/odu_status
# <odu_status version="1.7">
#     <odutype>proteushp</odutype>
#     <opstat>off</opstat>
#     <opmode>off</opmode>
#     <iducfm>0</iducfm>
#     <lat>na</lat>
#     <oducoiltmp>27</oducoiltmp>
#     <blwrpm>0</blwrpm>
#     <oat>27</oat>
#     <linevolt>237</linevolt>
#     <lockactive>off</lockactive>
#     <locktime>0</locktime>
#     <comprpm>0</comprpm>
#     <suctpress>91</suctpress>
#     <sucttemp>27</sucttemp>
#     <suctsupheat>0.0</suctsupheat>
#     <dischargetmp>92</dischargetmp>
#     <sparesensorstatus>sensor_status_invalid</sparesensorstatus>
#     <sparesensorvalue>na</sparesensorvalue>
#     <exvpos>0</exvpos>
#     <curtail>off</curtail>
#     <statpress>0.00</statpress>
#     <enterreftmp>0.00</enterreftmp>
#     <availminheatstage>2</availminheatstage>
#     <availmaxheatstage>5</availmaxheatstage>
#     <availmincoolstage>0</availmincoolstage>
#     <availmaxcoolstage>0</availmaxcoolstage>
#     <opminheatstage>2</opminheatstage>
#     <opmaxheatstage>5</opmaxheatstage>
#     <opmincoolstage>0</opmincoolstage>
#     <opmaxcoolstage>0</opmaxcoolstage>
# </odu_status>

# ODU (OutDoor Unit) Status Handler Map
request_map: Map = {
    "/odu_status/odutype": {
        "name": "outdoorUnitType",
        "handler": util.totext
    },
    "/odu_status/opmode": {
        "name": "mode",
        "handler": util.totext
    },
    "/odu_status/opstat": {
        "name": "?stat",
        "handler": util.totext
    },
    "/odu_status/iducfm": {
        "name": "inDoorUnitCFM",
        "handler": util.toint
    },
    "/odu_status/oducoiltmp": {
        "name": "coilTemperature",
        "handler": util.toint
    },
    "/odu_status/blwrpm": {
        "name": "blowerRPM",
        "handler": util.toint
    },
    "/odu_status/linevolt": {
        "name": "lineVoltage",
        "handler": util.toint
    },
    "/odu_status/comprpm": {
        "name": "?compressorRpm",
        "handler": util.toint
    },
    "/odu_status/suctpress": {
        "name": "?suctpress",
        "handler": util.toint
    },
    "/odu_status/sucttemp": {
        "name": "?sucttemp",
        "handler": util.toint
    },
    "/odu_status/suctsupheat": {
        "name": "?suctsupheat",
        "handler": util.tofloat
    },
    "/odu_status/dischargetmp": {
        "name": "dischargeTemperature",
        "handler": util.toint
    },
    "/odu_status/statpress": {
        "name": "staticPressure",
        "handler": util.tofloat
    },
}

class OduStatusHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = "/systems/([^/]+)/odu_status"
        self.type = DataSetType.OduStatus
        self.request_map = request_map
        self.response_map = { }

    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        dataset = await self.process_form_data(request)
        keys = { "serial_number": matches[0] }
        return ProcessingResult(self.type, keys, dataset)

    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        return ProcessingResult.Empty
