from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<time version="1.48" xmlns:atom="http://www.w3.org/2005/Atom">
    <atom:link rel="self" href="https://www.app-api.ing.carrier.com/time/" />
    <utc>2023-01-09T05:04:30.563Z</utc>
</time>
"""

class TimeHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "GET"
        self.url_template = r"/time"
        self.type = DataSetType.Time
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
