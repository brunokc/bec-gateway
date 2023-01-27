import re
import json
import logging
import xml.etree.ElementTree as ET

from abc import ABC, abstractmethod
from datetime import date, datetime
from enum import Enum
from pyproxy.httprequest import parse_form_data
from typing import Dict, List, NamedTuple, Any
from . import util

_LOGGER = logging.getLogger(__name__)

class DataSetType(Enum):
    Status = "status"
    IduStatus = "idu_status"
    OduStatus = "odu_status"
    PingRates = "ping_rates"


class DateTimeEncoder(json.JSONEncoder):
    """Special JSON encoder to deal with date/datetime representation"""
    # Override the default method
    def default(self, obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()


class BaseHandler(ABC):
    method: str
    url_template: str
    type: DataSetType
    request_map: dict
    response_map: dict

    async def get_form_data(self, request):
        _LOGGER.debug("handling %s for %s", self.method, self.url_template)
        body = await request.read_body()
        _LOGGER.debug("body (%d bytes): %s", len(body), body)

        form_data = parse_form_data(body)
        payload = form_data[b"data"]
        _LOGGER.debug("payload: %s", payload)
        return payload

    def process_xml_payload(self, xml, map):
        tree = ET.fromstring(xml)
        dataset = util.map_xml_payload(tree, map)
        return dataset

    async def process_form_data(self, request):
        form_data = await self.get_form_data(request)
        dataset = self.process_xml_payload(form_data, self.request_map)
        _LOGGER.debug("request json: %s", json.dumps(dataset))
        return dataset

    async def process_response_data(self, response):
        body = await response.read_body()
        _LOGGER.debug("response body (%d bytes): %s", len(body), body)
        dataset = self.process_xml_payload(body, self.response_map)
        _LOGGER.debug("response json: %s", json.dumps(dataset, cls=DateTimeEncoder))
        return dataset

    @abstractmethod
    async def process_request(self, matches, request):
        pass

    @abstractmethod
    async def process_response(self, matches, response):
        pass


class ProcessingResult(NamedTuple):
    type: DataSetType
    keys: dict[str, str]
    dataset: dict[str, Any]


from .status import StatusHandler
from .idustatus import IduStatusHandler
from .odustatus import OduStatusHandler

class ContentProcessor:
    def __init__(self):
        self._handlers: List[BaseHandler] = [
            StatusHandler(),
            IduStatusHandler(),
            OduStatusHandler()
        ]

    def _find_handler(self, request):
        for handler in self._handlers:
            if request.method == handler.method:
                match = re.match(handler.url_template, request.raw_url)
                if match:
                    return handler, list(match.groups())
        return None, None

    async def process_request(self, request):
        handler, matches = self._find_handler(request)
        if handler:
            _LOGGER.debug("request handler %s(%s:%s) selected", type(handler),
                handler.method, handler.url_template)
            return await handler.process_request(matches, request)
        return None

    async def process_response(self, request, response):
        handler, matches = self._find_handler(request)
        if handler:
            _LOGGER.debug("response handler %s(%s:%s) selected", type(handler),
                handler.method, handler.url_template)
            return await handler.process_response(matches, response)
        return None
