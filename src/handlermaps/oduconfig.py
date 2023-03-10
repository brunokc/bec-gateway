from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult


# ODU (OutDoor Unit) Config handler map
"""
<odu_config version="1.7">
    <odutype>proteushp</odutype>
    <oducoolafl>eff350</oducoolafl>
    <oduheatafl>eff350</oduheatafl>
    <dehumafl>normal</dehumafl>
    <coollocktemp>none</coollocktemp>
    <heatlocktemp>32</heatlocktemp>
    <lowambcool/>
    <quietshift/>
    <coollatchmode/>
    <coollatchtemp/>
    <heatlatchmode/>
    <heatlatchtemp/>
    <brownout/>
    <defrostbackup>off</defrostbackup>
    <maxrpm/>
    <defrostInt>auto</defrostInt>
    <curtailcool>disabled</curtailcool>
    <curtailheat>disabled</curtailheat>
    <lowaflmult/>
    <vcapfloorcfm/>
    <vcapceilingcfm/>
    <vcapcfmfloor/>
    <vcapcfmceiling/>
    <vcapcfmuplimit/>
    <cfmlimitsvalid/>
    <mincoolstage>1</mincoolstage>
    <maxcoolstage>5</maxcoolstage>
    <minheatstage>1</minheatstage>
    <maxheatstage>5</maxheatstage>
    <usermincoolstage>1</usermincoolstage>
    <usermaxcoolstage>5</usermaxcoolstage>
    <userminheatstage>1</userminheatstage>
    <usermaxheatstage>5</usermaxheatstage>
    <usercoollatch>95</usercoollatch>
    <userheatlatch>35</userheatlatch>
    <lockoutcount/>
    <flowratesetting/>
    <lpumppowersetting/>
    <freezelimit/>
</odu_config>
"""

class OduConfigHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/odu_config"
        self.type = DataSetType.OduConfig
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
