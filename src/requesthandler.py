from datetime import datetime, timezone
import logging
import re
from typing import Any, Callable, Optional

# For HTTP Date support
from time import mktime
from wsgiref.handlers import format_date_time

from pyproxy.callback import ProxyServerCallback, ProxyServerAction
from pyproxy.httprequest import HttpRequest, HttpResponse
from pyproxy.proxyserver import ProxyServer

from .datetimeutils import to_iso_format
from .handlermaps import ContentProcessor, DataSetType, ProcessingResult
from .statusresponsehandler import StatusResponseHandler

CallbackType = Optional[Callable[[ProcessingResult], None]]

_LOGGER = logging.getLogger(__name__)


class ConnexRequestHandler(ProxyServerCallback):
    def __init__(self, proxy_ip: str, proxy_port: int):
        self._callback: CallbackType = None
        self._content_processor = ContentProcessor()

        self._server = ProxyServer(proxy_ip, proxy_port)
        self._server.register_callback(self)

        self._last_activity_time = datetime.min

        self._status_response_handler = StatusResponseHandler()

        self._client_response_headers = {
            "Content-Type": "application/xml",
            "Content-Length": 0,
            "Connection": "keep-alive",
            # "Date": "Mon, 09 Jan 2023 0$PING_RATE$:04:36 GMT",
            # "Apigw-Requestid": "edX_riSuoAMEVGA=",
            # "X-Cache": "Miss from cloudfront",
            # "Via": "1.1 707e733794d52100fde0ab21bf0b1462.cloudfront.net (CloudFront)",
            # "X-Amz-Cf-Pop": "SEA73-P1",
            # "X-Amz-Cf-Id": "TeC6XU82YTaYOygAzyKjUWfv9hrsNinAl6cneJzqnVEzl01CBLv8Tg==",
        }

        self._status_response_template = (b'<status version="1.45" '
            b'xmlns:atom="http://www.w3.org/2005/Atom"><atom:link rel="self" '
            b'href="https://www.app-api.ing.carrier.com/systems/1117W005762/status"/>'
            b'<atom:link rel="http://www.api.ing.carrier.com/rels/system" '
            b'href="https://www.app-api.ing.carrier.com/systems/1117W005762"/>'
            b'<timestamp>$timestamp$</timestamp><pingRate>$pingRate$</pingRate>'
            b'<iduStatusPingRate>$iduStatusPingRate$</iduStatusPingRate>'
            b'<iduFaultsPingRate>$iduFaultsPingRate$</iduFaultsPingRate>'
            b'<oduStatusPingRate>$oduStatusPingRate$</oduStatusPingRate>'
            b'<oduFaultsPingRate>$oduFaultsPingRate$</oduFaultsPingRate>'
            b'<historyPingRate>$historyPingRate$</historyPingRate>'
            b'<equipEventsPingRate>$equipEventsPingRate$</equipEventsPingRate>'
            b'<rootCausePingRate>$rootCausePingRate$</rootCausePingRate>'
            b'<serverHasChanges>false</serverHasChanges><configHasChanges>false'
            b'</configHasChanges><dealerHasChanges>false</dealerHasChanges>'
            b'<dealerLogoHasChanges>false</dealerLogoHasChanges><oduConfigHasChanges>'
            b'false</oduConfigHasChanges><iduConfigHasChanges>false'
            b'</iduConfigHasChanges><utilityEventsHasChanges>false'
            b'</utilityEventsHasChanges><sensorConfigHasChanges>false'
            b'</sensorConfigHasChanges><sensorProfileHasChanges>false'
            b'</sensorProfileHasChanges><sensorDiagnosticHasChanges>false'
            b'</sensorDiagnosticHasChanges></status>')

    def _get_http_date(self) -> str:
        now = datetime.now()
        stamp = mktime(now.timetuple())
        return format_date_time(stamp)

    def _set_empty_response(self, response: HttpResponse, version: str) -> None:
        response.http_version = version
        response.response_code = 200
        response.response_text = "OK"
        response.headers.update(self._client_response_headers)
        response.headers["Date"] = self._get_http_date()
        response.set_body(b'')

    def _set_status_response(self, response: HttpResponse, version: str) -> None:
        response.http_version = version
        response.response_code = 200
        response.response_text = "OK"
        response.headers.update(self._client_response_headers)
        response.headers["Date"] = self._get_http_date()

        body = self._status_response_template
        body = body.replace(b"$timestamp$", to_iso_format(datetime.now()).encode())

        ping_rate = str(self._status_response_handler.ping_rate).encode()
        current_ping_rates = self._status_response_handler.get_ping_rates()
        for ping_rate_type in current_ping_rates:
            body = body.replace(f"${ping_rate_type}$".encode(), ping_rate)

        _LOGGER.debug("generated status response body (%d bytes): %s",
            len(body), body)
        response.set_body(body)

    @property
    def last_activity_time(self) -> datetime:
        return self._last_activity_time

    def register_callback(self, callback: CallbackType) -> None:
        self._callback = callback

    def set_ping_rate(self, rate: Optional[int]) -> None:
        self._status_response_handler.set_rate(rate)

    async def on_new_request_async(self, request: HttpRequest) -> ProxyServerAction:
        _LOGGER.debug("new request verb=%s path=%s", request.method, request.url.path)
        self._last_activity_time = datetime.now(timezone.utc)

        if not self._callback:
            return ProxyServerAction.Forward

        action = ProxyServerAction.Forward
        result = await self._content_processor.process_request(request)
        if result is None:
            _LOGGER.debug("no content processor handler found")
        else:
            if result != ProcessingResult.Empty:
                self._callback(result)

                # Based on the dataset type and how long ago we last received
                # data for this type, we'll either suppress the request to the
                # server (if it's too soon compared to the default ping rate) or
                # we'll let it pass (if it's been longer than the default ping rate)
                action = self._status_response_handler.get_action_for_dataset(result.type)
                _LOGGER.debug("action for dataset %s: %s", result.type.name, action.name)
        return action

    async def on_new_response_async(
        self,
        action: ProxyServerAction,
        request: HttpRequest,
        response: HttpResponse) -> None:

        _LOGGER.debug("on_new_response_async: action=%s verb=%s path=%s",
            action.name, request.method, request.url.path)
        self._last_activity_time = datetime.now(timezone.utc)

        if not self._callback:
            return

        if action == ProxyServerAction.Forward:
            result = await self._content_processor.process_response(request, response)
            if result is None:
                _LOGGER.debug("no content processor handler found for this dataset type")
            else:
                if result != ProcessingResult.Empty:
                    self._callback(result)

                if result.type == DataSetType.PingRates:
                    await self._status_response_handler.ingest(result, response)
        else:
            # If we suppressed the call up to the server, we're on the hook for
            # providing a response back to the client ourselves. For all currently
            # supported cases, we just need to send a dummy "200 OK" back to the
            # client.
            if request.url.path.endswith("/status"):
                self._set_status_response(response, request.version)

                # Pretend we got this response from the server and process it so
                # that we can ingest it and have the internal ping rates updated
                result = await self._content_processor.process_response(request, response)
                assert result is not None
                await self._status_response_handler.ingest(result, response)
            else:
                self._set_empty_response(response, request.version)

    async def run(self) -> None:
        await self._server.run()
