from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
POST /systems/1117W005762/energy
<energy version="1.7">
    <seer>15.0</seer>
    <hspf>8.8</hspf>
    <cooling display="on" enabled="on"/>
    <hpheat display="on" enabled="on"/>
    <eheat display="off" enabled="on"/>
    <gas display="on" enabled="on"/>
    <reheat display="off" enabled="on"/>
    <fangas display="on" enabled="on"/>
    <fan display="on" enabled="on"/>
    <looppump display="off" enabled="off"/>
    <usage>
        <period id="day1">
            <cooling>0</cooling>
            <hpheat>7</hpheat>
            <eheat>0</eheat>
            <gas>170</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>0</fan>
            <looppump>0</looppump>
        </period>
        <period id="day2">
            <cooling>0</cooling>
            <hpheat>10</hpheat>
            <eheat>0</eheat>
            <gas>97</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>0</fan>
            <looppump>0</looppump>
        </period>
        <period id="month1">
            <cooling>1</cooling>
            <hpheat>183</hpheat>
            <eheat>0</eheat>
            <gas>2725</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>0</fan>
            <looppump>0</looppump>
        </period>
        <period id="month2">
            <cooling>0</cooling>
            <hpheat>214</hpheat>
            <eheat>0</eheat>
            <gas>2238</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>0</fan>
            <looppump>0</looppump>
        </period>
        <period id="year1">
            <cooling>1</cooling>
            <hpheat>404</hpheat>
            <eheat>0</eheat>
            <gas>5133</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>0</fan>
            <looppump>0</looppump>
        </period>
        <period id="year2">
            <cooling>1905</cooling>
            <hpheat>1503</hpheat>
            <eheat>0</eheat>
            <gas>8828</gas>
            <reheat>0</reheat>
            <fangas>0</fangas>
            <fan>29</fan>
            <looppump>0</looppump>
        </period>
    </usage>
    <cost>
        <period id="day1">
            <cooling>0.00</cooling>
            <hpheat>0.89</hpheat>
            <eheat>0.00</eheat>
            <gas>2.71</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>0.00</fan>
            <looppump>0.00</looppump>
        </period>
        <period id="day2">
            <cooling>0.00</cooling>
            <hpheat>1.30</hpheat>
            <eheat>0.00</eheat>
            <gas>1.56</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>0.00</fan>
            <looppump>0.00</looppump>
        </period>
        <period id="month1">
            <cooling>0.10</cooling>
            <hpheat>24.30</hpheat>
            <eheat>0.00</eheat>
            <gas>43.70</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>0.00</fan>
            <looppump>0.00</looppump>
        </period>
        <period id="month2">
            <cooling>0.00</cooling>
            <hpheat>27.50</hpheat>
            <eheat>0.00</eheat>
            <gas>36.10</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>0.00</fan>
            <looppump>0.00</looppump>
        </period>
        <period id="year1">
            <cooling>0.00</cooling>
            <hpheat>53.00</hpheat>
            <eheat>0.00</eheat>
            <gas>83.00</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>0.00</fan>
            <looppump>0.00</looppump>
        </period>
        <period id="year2">
            <cooling>248.00</cooling>
            <hpheat>196.00</hpheat>
            <eheat>0.00</eheat>
            <gas>144.00</gas>
            <reheat>0.00</reheat>
            <fangas>0.00</fangas>
            <fan>1.00</fan>
            <looppump>0.00</looppump>
        </period>
    </cost>
</energy>
"""

class EnergyHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)/energy"
        self.type = DataSetType.Energy
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
