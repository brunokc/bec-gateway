from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<system_profile version="1.7">
    <pin>A7BD6B1F</pin>
    <brand>Bryant</brand>
    <model>SYSTXBBECC01-A</model>
    <serial>1117W005762</serial>
    <firmware>CESR131493-14.02</firmware>
    <routerMac>C404151BD3A3</routerMac>
    <idutype>furnace</idutype>
    <idusource>gas</idusource>
    <idustages>2</idustages>
    <iducapacity>71</iducapacity>
    <pwmblower>off</pwmblower>
    <indoorModel>315AAV048090AGJA</indoorModel>
    <indoorSerial>----------------</indoorSerial>
    <iduversion>CESR131557-24</iduversion>
    <odutype>multistghp</odutype>
    <oducapacity>48</oducapacity>
    <outdoorModel>288BNV048000FA</outdoorModel>
    <outdoorSerial>1817E36208</outdoorSerial>
    <oduversion>CESR131564-10</oduversion>
    <samType>ING</samType>
    <uvpresent>off</uvpresent>
    <humpresent>off</humpresent>
    <ventpresent>off</ventpresent>
    <sampresent>off</sampresent>
    <sammodel/>
    <samserial/>
    <samversion/>
    <nimpresent>off</nimpresent>
    <nimmodel/>
    <nimserial/>
    <nimversion/>
    <ewtsensorpresent>off</ewtsensorpresent>
    <zoneboards>
        <board id="1">
            <present>off</present>
            <model/>
            <serial/>
            <version/>
        </board>
        <board id="2">
            <present>off</present>
            <model/>
            <serial/>
            <version/>
        </board>
    </zoneboards>
    <zones>
        <zone id="1">
            <present>on</present>
            <sensortype>user interface</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="2">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="3">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="4">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="5">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="6">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="7">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
        <zone id="8">
            <present>off</present>
            <sensortype>remote sensor</sensortype>
            <ssmodel>N/A</ssmodel>
            <ssserial>N/A</ssserial>
            <ssversion>N/A</ssversion>
        </zone>
    </zones>
</system_profile>
"""

class ProfileHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/profile"
        self.type = DataSetType.Profile
        # self.request_map = request_map
        # self.response_map = response_map

    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        # dataset = await self.process_form_data(request)
        # keys = { "serial_number": matches[0] }
        # return ProcessingResult(self.type, keys, dataset)
        return ProcessingResult.Empty

    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        # dataset = await self.process_response_data(response)
        # keys = { "serial_number": matches[0] }
        # return ProcessingResult(DataSetType.PingRates, keys, dataset)
        return ProcessingResult.Empty
