from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
GET /weather/98052/forecast
<weather_forecast version="1.48" xmlns:atom="http://www.w3.org/2005/Atom">
    <atom:link rel="self" href="https://www.app-api.ing.carrier.com/weather/98052/forecast" />
    <atom:link rel="http://www.api.ing.carrier.com/rels/weather"
        href="https://www.app-api.ing.carrier.com/weather/98052" />
    <timestamp>2023-01-09T05:04:29.066Z</timestamp>
    <ping>240</ping>
    <day id="Sunday">
        <timestamp>2023-01-08T07:00:00-08:00</timestamp>
        <min_temp units="f">41</min_temp>
        <max_temp units="f">49</max_temp>
        <pop>85</pop>
        <status_id>8</status_id>
        <status_message>Light Rain</status_message>
    </day>
    <day id="Monday">
        <timestamp>2023-01-09T07:00:00-08:00</timestamp>
        <min_temp units="f">42</min_temp>
        <max_temp units="f">48</max_temp>
        <pop>85</pop>
        <status_id>8</status_id>
        <status_message>Light Rain</status_message>
    </day>
    <day id="Tuesday">
        <timestamp>2023-01-10T07:00:00-08:00</timestamp>
        <min_temp units="f">39</min_temp>
        <max_temp units="f">50</max_temp>
        <pop>24</pop>
        <status_id>8</status_id>
        <status_message>Rain Showers</status_message>
    </day>
    <day id="Wednesday">
        <timestamp>2023-01-11T07:00:00-08:00</timestamp>
        <min_temp units="f">45</min_temp>
        <max_temp units="f">48</max_temp>
        <pop>85</pop>
        <status_id>8</status_id>
        <status_message>Rain</status_message>
    </day>
    <day id="Thursday">
        <timestamp>2023-01-12T07:00:00-08:00</timestamp>
        <min_temp units="f">46</min_temp>
        <max_temp units="f">49</max_temp>
        <pop>99</pop>
        <status_id>8</status_id>
        <status_message>Rain</status_message>
    </day>
    <day id="Friday">
        <timestamp>2023-01-13T07:00:00-08:00</timestamp>
        <min_temp units="f">45</min_temp>
        <max_temp units="f">52</max_temp>
        <pop>89</pop>
        <status_id>8</status_id>
        <status_message>Light Rain</status_message>
    </day>
</weather_forecast>
"""

class WeatherForecastHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "GET"
        self.url_template = r"/weather/(\d+)/forecast"
        self.type = DataSetType.WeatherForecast
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
