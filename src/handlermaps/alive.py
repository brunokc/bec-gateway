from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
GET /Alive?sn=1117W005762
alive
"""

class AliveHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "GET"
        self.url_template = r"/Alive?sn=(.+)"
        self.type = DataSetType.Alive
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
