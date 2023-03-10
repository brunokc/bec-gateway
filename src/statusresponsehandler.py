from datetime import datetime, timezone
import logging
import re
from typing import Any, Callable, Dict, Optional

from pyproxy.callback import ProxyServerAction
from pyproxy.httprequest import HttpResponse

from . import datetimeutils
from .handlermaps import DataSetType, ProcessingResult

CallbackType = Optional[Callable[[ProcessingResult], None]]

_LOGGER = logging.getLogger(__name__)


class StatusResponseHandler:
    def __init__(self):
        self._last_updated = datetimeutils.utcmin
        self._dataset_type_map: Dict[DataSetType, str] = {
            DataSetType.EquipmentEvents: "equipEventsPingRate",
            DataSetType.History: "historyPingRate",
            DataSetType.IduFaults: "iduFaultsPingRate",
            DataSetType.IduStatus: "iduStatusPingRate",
            DataSetType.OduFaults: "oduFaultsPingRate",
            DataSetType.OduStatus: "oduStatusPingRate",
            DataSetType.RootCause: "rootCausePingRate",
            DataSetType.Status: "pingRate",
        }
        self._ping_rates: Dict[str, int] = { }
        self._ping_rate: Optional[int] = None

    def get_ping_rates(self) -> Dict[str, int]:
        return self._ping_rates

    @property
    def ping_rate(self) -> Optional[int]:
        return self._ping_rate

    def set_rate(self, rate: Optional[int]) -> None:
        _LOGGER.debug("ping rate set to %d", rate)
        self._ping_rate = rate

    def _update_ping_rates(self, dataset):
        now = datetime.now(timezone.utc)

        # Filter results to just the ping rates
        ping_rates = { k:v for k, v in dataset.items() if k.endswith("Rate") }
        _LOGGER.debug("filtered ping rates: %s", ping_rates)

        if self._last_updated == datetimeutils.utcmin:
            self._ping_rates.update(ping_rates)
        else:
            elapsed_time = now - self._last_updated
            assert len(self._ping_rates) == len(ping_rates)
            for k in self._ping_rates:
                self._ping_rates[k] = max(0, self._ping_rates[k] - elapsed_time.seconds)
            _LOGGER.debug("current ping rates left: %s", self._ping_rates)

        self._last_updated = now

    def _select_ping_rate(self, body):
        assert self._ping_rate is not None
        if self._ping_rate > 0:
            ping_rate = self._ping_rate
        else:
            match = re.search(rb"<pingRate>(\d+)</pingRate>", body)
            assert match
            ping_rate = int(match.group(1))
        return ping_rate

    async def ingest(self, result: ProcessingResult, response: HttpResponse) -> ProxyServerAction:
        assert result.type == DataSetType.PingRates
        if self._ping_rate is not None:
            self._update_ping_rates(result.dataset)

            # To ensure thermostats will send all data they have in short order,
            # we simulate short ping rates until told to go back to normal.
            #
            # Replace all ping rates to a short time. Ping rates come embedded in an
            # XML response from the server from the "status" request. Ping rates take
            # the form:
            # <iduStatusPingRate>93600</iduStatusPingRate>
            # This function just replaces whatever number value with a configured
            # value.
            body = await response.read_body()
            ping_rate = self._select_ping_rate(body)

            _LOGGER.debug("overriding ping rate to %d", ping_rate)
            _LOGGER.debug("body before replacements (%d bytes): %s", len(body), body)
            body = re.sub(rb"PingRate>(\d+)</", f"PingRate>{ping_rate}</".encode(), body)
            _LOGGER.debug("body after replacements (%d bytes): %s", len(body), body)
            response.set_body(body)

        return ProxyServerAction.Forward

    def get_action_for_dataset(self, dataset_type: DataSetType) -> ProxyServerAction:
        ping_rate_type = self._dataset_type_map.get(dataset_type, None)
        _LOGGER.debug("ping_rate_type: %s (%s)", ping_rate_type,
            "present" if ping_rate_type in self._ping_rates else "missing")

        if ping_rate_type is not None and ping_rate_type in self._ping_rates:
            current_ping_rate = self._ping_rates[ping_rate_type]
            _LOGGER.debug("ping rate timeout left for %s: %d sec", dataset_type.name,
                current_ping_rate)
            if current_ping_rate > 0:
                _LOGGER.debug("suppressing proxy server call due unexpired timeout")
                return ProxyServerAction.Suppress

        return ProxyServerAction.Forward
