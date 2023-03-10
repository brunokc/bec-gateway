from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<utility_events version="1.48" xmlns:atom="http://www.w3.org/2005/Atom">
    <atom:link rel="self" href="https://www.app-api.ing.carrier.com/systems/1117W005762/utility_events" />
    <atom:link rel="http://www.api.ing.carrier.com/rels/system"
        href="https://www.app-api.ing.carrier.com/systems/1117W005762" />
    <events />
</utility_events>
"""

class UtilityEventsHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "GET"
        self.url_template = r"/systems/([^/]+)/utility_events"
        self.type = DataSetType.UtilityEvents
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
