import logging
import re

from abc import ABC, abstractmethod
from enum import Enum
from pyproxy.httprequest import parse_form_data, HttpRequest, HttpResponse
from typing import Any, Callable, ClassVar, Dict, List, NamedTuple, Optional, Tuple
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

from .. import jsonutils

_LOGGER = logging.getLogger(__name__)

class DataSetType(Enum):
    Unset = "unset"
    Status = "status"
    IduStatus = "idu_status"
    OduStatus = "odu_status"
    PingRates = "ping_rates"


Map = Dict[str, Dict[str, Any]]
Handler = Callable[[Element], Any]

from . import util

class _ProcessingResult(NamedTuple):
    type: DataSetType
    keys: dict[str, str]
    dataset: dict[str, Any]

class ProcessingResult(_ProcessingResult):
    Empty: ClassVar["ProcessingResult"]

ProcessingResult.Empty = ProcessingResult(DataSetType.Unset, { }, { })



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
        dataset = self.process_xml_payload(form_data, self.request_map)
        _LOGGER.debug("request json: %s", jsonutils.dumps(dataset))
        return dataset

    async def process_response_data(self, response: HttpResponse) -> Dict[str, Any]:
        body = await response.read_body()
        _LOGGER.debug("response body (%d bytes): %s", len(body), body)
        dataset = self.process_xml_payload(body.decode(), self.response_map)
        _LOGGER.debug("response json: %s", jsonutils.dumps(dataset))
        return dataset

    @abstractmethod
    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        pass

    @abstractmethod
    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        pass


from .status import StatusHandler
from .idustatus import IduStatusHandler
from .odustatus import OduStatusHandler

class ContentProcessor:
    def __init__(self) -> None:
        self._handlers: List[BaseHandler] = [
            StatusHandler(),
            IduStatusHandler(),
            OduStatusHandler()
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
            _LOGGER.debug("request handler %s(%s:%s) selected", type(handler),
                handler.method, handler.url_template)
            return await handler.process_request(matches, request)
        return None

    async def process_response(self, request: HttpRequest, response: HttpResponse) -> Optional[ProcessingResult]:
        handler, matches = self._find_handler(request)
        if handler and matches:
            _LOGGER.debug("response handler %s(%s:%s) selected", type(handler),
                handler.method, handler.url_template)
            return await handler.process_response(matches, response)
        return None
