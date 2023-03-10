from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult


# IDU (InDoor Unit) Config handler map
"""
<idu_config version="1.7">
    <idutype>furnace2stg</idutype>
    <iduairflow>comfort</iduairflow>
    <gtermavail>on</gtermavail>
    <gtermsetting>disabled</gtermsetting>
    <gtermtype>closed</gtermtype>
    <gtermfan>low</gtermfan>
    <gtermlabel1>AUXILIARY</gtermlabel1>
    <gtermlabel2>INPUT (G)</gtermlabel2>
    <gtermlabel3>ALERT</gtermlabel3>
    <heatoffdelay>120</heatoffdelay>
    <auxheatlocktmp>50</auxheatlocktmp>
    <reheat/>
    <dehumdrain>15</dehumdrain>
    <mincfm/>
    <maxcfm/>
    <absmincfm/>
    <absmaxcfm/>
    <mincfmenable/>
    <maxcfmenable/>
    <furnstages>system</furnstages>
    <pwmadjust>1</pwmadjust>
    <hydronicafl/>
    <hydronicondelay/>
    <hydronicoffdelay/>
    <lowheatrise>off</lowheatrise>
    <altitudeselect>0</altitudeselect>
    <elevation>800</elevation>
</idu_config>
"""

class IduConfigHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/idu_config"
        self.type = DataSetType.IduConfig
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
