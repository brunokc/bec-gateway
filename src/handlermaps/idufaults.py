from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<idu_faults version="1.7">
    <source>furnace</source>
    <faults>
        <fault>
            <code>12</code>
            <description>12-BLOWER ON AFTER AFTER POWER UP</description>
            <occurrences>1</occurrences>
        </fault>
        <fault>
            <code>25</code>
            <description>25-INVALID MODEL</description>
            <occurrences>4</occurrences>
        </fault>
    </faults>
</idu_faults>
"""

class IduFaultsHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/idu_faults"
        self.type = DataSetType.IduFaults
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
