from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<updates xmlns="http://schema.ota.carrier.com">
    <update>
        <type>thermostat</type>
        <model>SYSTXCCITC01-A</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccit-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXCCITW01-A</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccit-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXBBECC01-A</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbec-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXBBECW01-A</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbec-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXCCITC01</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccit-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXCCITW01</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccit-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccit-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXBBECC01</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbec-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXBBECW01</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>14.02</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbec-14.02.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbec-14.02.html</url>
        </releaseNotes>
    </update>    <!--BING Variants-->
    <update>        <!-- Carrier model; English; black enclosure -->
        <type>thermostat</type>
        <model>SYSTXCCITC01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccitc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Carrier model; French; black enclosure -->
        <type>thermostat</type>
        <model>SYSTXCCICF01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccitc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Carrier model; English; white enclosure -->
        <type>thermostat</type>
        <model>SYSTXCCWIC01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccitc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Carrier model; French; white enclosure -->
        <type>thermostat</type>
        <model>SYSTXCCWIF01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxccitc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxccitc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Bryant model; English; black enclosure -->
        <type>thermostat</type>
        <model>SYSTXBBECC01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbecc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Bryant model; French; black enclosure -->
        <type>thermostat</type>
        <model>SYSTXBBECF01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbecc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Bryant model; English; white enclosure -->
        <type>thermostat</type>
        <model>SYSTXBBWEC01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbecc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!-- Bryant model; French; white enclosure -->
        <type>thermostat</type>
        <model>SYSTXBBWEF01-B</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/systxbbecc01-b-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/systxbbecc01-b-04.31.html</url>
        </releaseNotes>
    </update>
    <update>        <!--Ion model; English; black enclosure -->
        <type>thermostat</type>
        <model>SYST0101CW</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>4.31</version>
        <url>http://www.ota.ing.carrier.com/updates/syst0101cw-04.31.hex</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/syst0101cw-04.31.txt</url>
            <url type="text/html" locale="en-us">http://www.ota.ing.carrier.com/releaseNotes/syst0101cw-04.31.html</url>
        </releaseNotes>
    </update>    <!--CING Variants-->
    <update>
        <type>thermostat</type>
        <model>SYSTXCCITC01-C</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>01.22</version>
        <url>https://www.ota.ing.carrier.com/updates/CINF0122.BEX</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">https://www.ota.ing.carrier.com/releaseNotes/SYSTXCCITC01-C-01.22.txt</url>
            <url type="text/html" locale="en-us">https://www.ota.ing.carrier.com/releaseNotes/SYSTXCCITC01-C-01.22.html</url>
        </releaseNotes>
    </update>
    <update>
        <type>thermostat</type>
        <model>SYSTXBBECC01-C</model>
        <locales>
            <locale>en-us</locale>
        </locales>
        <version>01.22</version>
        <url>https://www.ota.ing.carrier.com/updates/CINF0122.BEX</url>
        <releaseNotes>
            <url type="text/plain" locale="en-us">https://www.ota.ing.carrier.com/releaseNotes/SYSTXBBECC01-C-01.22.txt</url>
            <url type="text/html" locale="en-us">https://www.ota.ing.carrier.com/releaseNotes/SYSTXBBECC01-C-01.22.html</url>
        </releaseNotes>
    </update>
</updates>
"""

class ManifestHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "GET"
        self.url_template = r"/manifest"
        self.type = DataSetType.Manifest
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
