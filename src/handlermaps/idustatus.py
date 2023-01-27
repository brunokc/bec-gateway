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

# IDU (Inside D Unit) Status handler map
request_map = {
    "/idu_status/idutype": {
        "name": "indoorUnitType",
        "handler": util.totext
    },
    "/idu_status/pwmblower": {
        "name": "?pwmBlower",
        "handler": util.totext
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
    def __init__(self):
        self.method = "POST"
        self.url_template = "/systems/([^/]+)/idu_status"
        self.type = DataSetType.IduStatus
        self.request_map = request_map
        self.response_map = { }

    async def process_request(self, matches, request):
        dataset = await self.process_form_data(request)
        keys = { "serial_number": matches[0] }
        return ProcessingResult(self.type, keys, dataset)

    async def process_response(self, matches, response):
        return { }
