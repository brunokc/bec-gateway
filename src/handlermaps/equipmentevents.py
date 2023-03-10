from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<equipment_events version="1.7">
    <events>
        <event id="1">
            <code>67</code>
            <source>HP</source>
            <description>67-STATOR HEATER FAULT</description>
            <localtime>2023-01-08T14:32:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="2">
            <code>210</code>
            <source>UI</source>
            <description>210-EXCESSIVE STATIC PRESS ENCOUNTERED</description>
            <localtime>2023-01-07T13:10:00</localtime>
            <occurrences>127</occurrences>
            <active>off</active>
        </event>
        <event id="3">
            <code>76</code>
            <source>HP</source>
            <description>76-FAN INVERTER LOCKOUT</description>
            <localtime>2022-11-30T02:12:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="4">
            <code>12</code>
            <source>furnace</source>
            <description>12-BLOWER ON AFTER AFTER POWER UP</description>
            <localtime>2022-11-30T01:21:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="5">
            <code>76</code>
            <source>HP</source>
            <description>76-FAN INVERTER LOCKOUT</description>
            <localtime>2022-11-29T23:20:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="6">
            <code>210</code>
            <source>UI</source>
            <description>210-EXCESSIVE STATIC PRESS ENCOUNTERED</description>
            <localtime>2022-11-29T22:55:00</localtime>
            <occurrences>127</occurrences>
            <active>off</active>
        </event>
        <event id="7">
            <code>68</code>
            <source>HP</source>
            <description>68-10 MIN STAGE 2 WARMUP DELAY</description>
            <localtime>2022-09-29T16:43:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="8">
            <code>179</code>
            <source>UI</source>
            <description>OUTDOOR UNIT COMMUNICATION FAULT</description>
            <localtime>2022-09-29T15:47:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
        <event id="9">
            <code>210</code>
            <source>UI</source>
            <description>210-EXCESSIVE STATIC PRESS ENCOUNTERED</description>
            <localtime>2022-09-28T06:52:00</localtime>
            <occurrences>127</occurrences>
            <active>off</active>
        </event>
        <event id="10">
            <code>41</code>
            <source>furnace</source>
            <description>41-BLOWER MOTOR FAULT</description>
            <localtime>2021-12-30T03:30:00</localtime>
            <occurrences>1</occurrences>
            <active>off</active>
        </event>
    </events>
</equipment_events>
"""

class EquipmentEventsHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/equipment_events"
        self.type = DataSetType.EquipmentEvents
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
