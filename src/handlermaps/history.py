from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<history version="1.7">
    <idu>
        <powercycles>4</powercycles>
        <lowheatcycles>395</lowheatcycles>
        <medheatcycles/>
        <highheatcycles>269</highheatcycles>
        <blowercycles>1102</blowercycles>
        <onhours>1792</onhours>
        <lowheathours>104</lowheathours>
        <medheathours/>
        <highheathours>47</highheathours>
        <blowerhours>428</blowerhours>
    </idu>
    <odu>
        <powercycles>6</powercycles>
        <lowcoolcycles/>
        <highcoolcycles>22347</highcoolcycles>
        <lowheatcycles/>
        <highheatcycles>46819</highheatcycles>
        <defrostcycles>467</defrostcycles>
        <lowventcycles/>
        <highventcycles/>
        <onhours>47633</onhours>
        <lowcoolhours/>
        <highcoolhours>6202</highcoolhours>
        <lowheathours/>
        <highheathours>7268</highheathours>
        <defrosthours>32</defrosthours>
        <lowventhours/>
        <highventhours/>
    </odu>
</history>
"""

class HistoryHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/history"
        self.type = DataSetType.History
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
