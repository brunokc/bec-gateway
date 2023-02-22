import json
import logging

from pyproxy.callback import ProxyServerCallback, ProxyServerAction
from pyproxy.httprequest import HttpRequest, HttpResponse
from pyproxy.proxyserver import ProxyServer
from typing import Callable, Optional

from .handlermaps import ContentProcessor, ProcessingResult, util

CallbackType = Optional[Callable[[ProcessingResult], None]]

_LOGGER = logging.getLogger(__name__)


class ConnexRequestHandler(ProxyServerCallback):
    def __init__(self, proxy_ip: str, proxy_port: int):
        # self.proxy_ip = proxy_ip
        # self.proxy_port = proxy_port
        self._callback: CallbackType = None
        self._content_processor = ContentProcessor()

        self._server = ProxyServer(proxy_ip, proxy_port)
        self._server.register_callback(self)


    def register_callback(self, callback: CallbackType) -> None:
        self._callback = callback

    # """Convert URL encoded HTML form data into a dictionary"""
    # def parse_form_data(self, form_data):
    #     values = { k:urllib.parse.unquote(v) for (k,v) in
    #         [entry.split(b"=") for entry in form_data.split(b"&")]
    #     }
    #     return values

    # async def get_mapped_data_from_request(self, request, handler):
    #     _LOGGER.debug("handling %s for %s", handler.method, handler.path)
    #     body = await request.read_body()
    #     _LOGGER.debug("body (%d bytes): %s", len(body), body)

    #     form_data = self.parse_form_data(body)
    #     payload = form_data[b"data"]
    #     _LOGGER.debug("payload: %s", payload)

    #     tree = ET.fromstring(payload)
    #     dataset = util.map_xml_payload(tree, handler.request_map)
    #     _LOGGER.debug("state: %s", json.dumps(dataset))

    #     return dataset

    async def on_new_request_async(self, request: HttpRequest) -> ProxyServerAction:
        _LOGGER.debug("new request verb=%s path=%s", request.method, request.url.path)

        if self._callback:
            result = await self._content_processor.process_request(request)
            if result is not None and result != ProcessingResult.Empty:
                self._callback(result)

        return ProxyServerAction.Forward

    async def on_new_response_async(
        self, request: HttpRequest, response: HttpResponse) -> ProxyServerAction:

        _LOGGER.debug("new response verb=%s path=%s", request.method, request.url.path)

        if self._callback:
            result = await self._content_processor.process_response(request, response)
            if result is not None and result != ProcessingResult.Empty:
                self._callback(result)

        return ProxyServerAction.Forward

    async def run(self) -> None:
        await self._server.run()
