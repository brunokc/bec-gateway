from pyproxy.httprequest import HttpRequest, HttpResponse
from typing import Any, Dict, List
from xml.etree.ElementTree import Element

from . import util
from . import BaseHandler, DataSetType, Handler, ProcessingResult

# <name>ZONE 1</name>
# <enabled>on</enabled>
# <currentActivity>manual</currentActivity>
# <rt>67.0</rt>
# <rh>34</rh>
# <fan>off</fan>
# <htsp>66.0</htsp>
# <clsp>70.0</clsp>
# <hold>on</hold>
# <otmr/>
# <zoneconditioning>idle</zoneconditioning>
# <damperposition>15</damperposition>
zone_info_request_map = {
    "./name": {
        "name": "name",
        "handler": util.totext
    },
    "./enabled": {
        "name": "enabled",
        "handler": util.tobool
    },
    "./currentActivity": {
        "name": "currentActivity",
        "handler": util.totext
    },
    "./rt": {
        "name": "temperature",
        "handler": util.tofloat
    },
    "./rh": {
        "name": "humidity",
        "handler": util.toint
    },
    "./fan": {
        "name": "fanOn",
        "handler": util.tobool
    },
    "./htsp": {
        "name": "heatSetpoint",
        "handler": util.tofloat
    },
    "./clsp": {
        "name": "coolSetpoint",
        "handler": util.tofloat
    },
    "./hold": {
        "name": "hold",
        "handler": util.tobool
    },
    "./zoneconditioning": {
        "name": "zoneConditioning",
        "handler": util.totext
    }
}

def handle_zone(node: Element) -> Dict[str, Any]:
    status: Dict[str, Any] = { }
    for k, v in zone_info_request_map.items():
        subNode = util.findnode(node, k)
        name = v["name"]
        handler = v["handler"]
        status.update({ name: handler(subNode) })
    return status

def handle_zones(node: Element) -> List[Dict[str, Any]]:
    zones = []
    for zoneNode in node:
        zone = {
            "id": zoneNode.get("id")
        }
        zone.update(handle_zone(zoneNode))
        zones.append(zone)
    return zones

# Status Handler Map
# (includes zones status)
request_map = {
    "/status/mode": {
        "name": "mode",
        "handler": util.totext
    },
    "/status/cfgtype": {
        "name": "configType",
        "handler": util.totext
    },
    "/status/oat": {
        "name": "outsideAirTemperature",
        "handler": util.toint
    },
    "/status/cfgem": {
        "name": "temperatureUnit",
        "handler": util.totext
    },
    "/status/filtrlvl": {
        "name": "filterUsageLevel",
        "handler": util.toint
    },
    "/status/zones": {
        "name": "zones",
        "handler": handle_zones
    },
}

response_map = {
    "/status/timestamp": {
        "name": "timestamp",
        "handler": util.todatetime
    },
    "/status/pingRate": {
        "name": "pingRate",
        "handler": util.toint
    },
    "/status/iduStatusPingRate": {
        "name": "iduStatusPingRate",
        "handler": util.toint
    },
    "/status/iduFaultsPingRate": {
        "name": "iduFaultsPingRate",
        "handler": util.toint
    },
    "/status/oduStatusPingRate": {
        "name": "oduStatusPingRate",
        "handler": util.toint
    },
    "/status/oduFaultsPingRate": {
        "name": "oduFaultsPingRate",
        "handler": util.toint
    },
    "/status/historyPingRate": {
        "name": "historyPingRate",
        "handler": util.toint
    },
    "/status/equipEventsPingRate": {
        "name": "equipEventsPingRate",
        "handler": util.toint
    },
    "/status/rootCausePingRate": {
        "name": "rootCausePingRate",
        "handler": util.toint
    },

    "/status/configHasChanges": {
        "name": "configHasChanges",
        "handler": util.tobool
    },
    "/status/dealerHasChanges": {
        "name": "dealerHasChanges",
        "handler": util.tobool
    },
    "/status/dealerLogoHasChanges": {
        "name": "dealerLogoHasChanges",
        "handler": util.tobool
    },
    "/status/oduConfigHasChanges": {
        "name": "oduConfigHasChanges",
        "handler": util.tobool
    },
    "/status/iduConfigHasChanges": {
        "name": "iduConfigHasChanges",
        "handler": util.tobool
    },
    "/status/utilityEventsHasChanges": {
        "name": "utilityEventsHasChanges",
        "handler": util.tobool
    },
    "/status/sensorConfigHasChanges": {
        "name": "sensorConfigHasChanges",
        "handler": util.tobool
    },
    "/status/sensorProfileHasChanges": {
        "name": "sensorProfileHasChanges",
        "handler": util.tobool
    },
    "/status/sensorDiagnosticHasChanges": {
        "name": "sensorDiagnosticHasChanges",
        "handler": util.tobool
    },
}

class StatusHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = "/systems/([^/]+)/status"
        self.type = DataSetType.Status
        self.request_map = request_map
        self.response_map = response_map

    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        dataset = await self.process_form_data(request)
        keys = { "serial_number": matches[0] }
        return ProcessingResult(self.type, keys, dataset)

    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        dataset = await self.process_response_data(response)
        keys = { "serial_number": matches[0] }
        return ProcessingResult(DataSetType.PingRates, keys, dataset)
