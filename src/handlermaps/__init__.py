import logging
import re

from abc import ABC, abstractmethod
from enum import Enum
from pyproxy import HttpRequest, HttpResponse, parse_form_data
from typing import Any, Callable, ClassVar, Dict, List, NamedTuple, Optional, Tuple
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from .. import jsonutils

_LOGGER = logging.getLogger(__name__)

class DataSetType(Enum):
    Unset = "unset"
    Alive = "alive"
    Dealer = "dealer"
    Energy = "energy"
    EquipmentEvents = "equipment_events"
    History = "history"
    IduConfig = "idu_config"
    IduFaults = "idu_faults"
    IduStatus = "idu_status"
    Manifest = "manifest"
    OduConfig = "odu_config"
    OduFaults = "odu_faults"
    OduStatus = "odu_status"
    Profile = "profile"
    RootCause = "root_cause"
    Status = "status"
    PingRates = "ping_rates"
    System = "system"
    Time = "time"
    UtilityEvents = "utility_events"
    WeatherForecast = "weather/forecast"


Map = Dict[str, Dict[str, Any]]
Handler = Callable[[Element], Any]

from . import util

class _ProcessingResult(NamedTuple):
    type: DataSetType = DataSetType.Unset
    keys: dict[str, str] = {}
    dataset: dict[str, Any] = {}

class ProcessingResult(_ProcessingResult):
    Empty: ClassVar["ProcessingResult"]

    def is_empty(self) -> bool:
        return len(self.dataset) == 0

ProcessingResult.Empty = ProcessingResult()


class BaseHandler(ABC):
    method: str
    url_template: str
    type: DataSetType
    request_map: Map
    response_map: Map

    async def get_form_data(self, request: HttpRequest) -> str:
        _LOGGER.debug("handling %s for %s", self.method, self.url_template)
        body = await request.read_body()
        _LOGGER.debug("body (%d bytes): %s", len(body), body)

        payload = ""
        if body:
            form_data = parse_form_data(body)
            payload = form_data[b"data"]
            _LOGGER.debug("payload: %s", payload)

        return payload

    def process_xml_payload(self, xml: str, map: Map) -> Dict[str, Handler]:
        tree = ET.fromstring(xml)
        dataset = util.map_xml_payload(tree, map)
        return dataset

    async def process_form_data(self, request: HttpRequest) -> Dict[str, Any]:
        form_data = await self.get_form_data(request)
        dataset = {}
        if form_data:
            dataset = self.process_xml_payload(form_data, self.request_map)
            _LOGGER.debug("request json: %s", jsonutils.dumps(dataset))
        return dataset

    async def process_response_data(self, response: HttpResponse) -> Dict[str, Any]:
        body = await response.read_body()
        _LOGGER.debug("response body (%d bytes): %s", len(body), body)
        dataset = {}
        if body:
            dataset = self.process_xml_payload(body.decode(), self.response_map)
        _LOGGER.debug("response json: %s", jsonutils.dumps(dataset))
        return dataset

    @abstractmethod
    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        pass

    @abstractmethod
    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        pass


from .alive import AliveHandler
from .dealer import DealerHandler
from .energy import EnergyHandler
from .equipmentevents import EquipmentEventsHandler
from .history import HistoryHandler
from .iduconfig import IduConfigHandler
from .idufaults import IduFaultsHandler
from .idustatus import IduStatusHandler
from .manifest import ManifestHandler
from .oduconfig import OduConfigHandler
from .odufaults import OduFaultsHandler
from .odustatus import OduStatusHandler
from .profile import ProfileHandler
from .rootcause import RootCauseHandler
from .status import StatusHandler
from .system import SystemHandler
from .time import TimeHandler
from .utilityevents import UtilityEventsHandler
from .weatherforecast import WeatherForecastHandler

class ContentProcessor:
    def __init__(self) -> None:
        self._handlers: List[BaseHandler] = [
            AliveHandler(),
            DealerHandler(),
            EnergyHandler(),
            EquipmentEventsHandler(),
            HistoryHandler(),
            IduConfigHandler(),
            IduFaultsHandler(),
            IduStatusHandler(),
            ManifestHandler(),
            OduConfigHandler(),
            OduFaultsHandler(),
            OduStatusHandler(),
            ProfileHandler(),
            RootCauseHandler(),
            StatusHandler(),
            SystemHandler(),
            TimeHandler(),
            UtilityEventsHandler(),
            WeatherForecastHandler(),
        ]

    def _find_handler(self, request: HttpRequest) -> Tuple[Optional[BaseHandler], Optional[List[str]]]:
        for handler in self._handlers:
            if request.method == handler.method:
                match = re.match(handler.url_template, request.raw_url)
                if match:
                    return handler, list(match.groups())
        return None, None

    async def process_request(self, request: HttpRequest) -> Optional[ProcessingResult]:
        handler, matches = self._find_handler(request)
        if handler and matches:
            _LOGGER.debug("request handler %s(%s:%s) selected", type(handler).__name__,
                handler.method, handler.url_template)
            return await handler.process_request(matches, request)
        return None

    async def process_response(self, request: HttpRequest, response: HttpResponse) -> Optional[ProcessingResult]:
        handler, matches = self._find_handler(request)
        if handler and matches:
            _LOGGER.debug("response handler %s(%s:%s) selected", type(handler).__name__,
                handler.method, handler.url_template)
            return await handler.process_response(matches, response)
        return None
