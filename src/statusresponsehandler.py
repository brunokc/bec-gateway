from dataclasses import dataclass
from datetime import datetime, timezone
import logging
import re
from typing import Any, Callable, Dict, Optional

from pyproxy import HttpResponse, ProxyServerAction

from . import datetimeutils
from .handlermaps import DataSetType, ProcessingResult

CallbackType = Optional[Callable[[ProcessingResult], None]]

_LOGGER = logging.getLogger(__name__)


@dataclass
class PingRateInfo:
    last_updated: datetime = datetimeutils.utcmin
    ping_rate: int = 0

    def __repr__(self):
        return f"{self.ping_rate} ({datetimeutils.to_iso_format(self.last_updated)})"

class StatusResponseHandler:
    def __init__(self) -> None:
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
        self._ping_rates: Dict[str, PingRateInfo] = { }
        self._service_ping_rates: Dict[str, int] = { }
        self._ping_rate: Optional[int] = None

        for v in self._dataset_type_map.values():
            self._ping_rates[v] = PingRateInfo()

    def get_ping_rates(self) -> Dict[str, int]:
        return self._ping_rates

    @property
    def ping_rate(self) -> Optional[int]:
        return self._ping_rate

    def set_rate(self, rate: Optional[int]) -> None:
        """
        Possible ping rate values:
        None: use ping rates as suggested by the service (i.e.: don't  interfere)
           0: use the general ping rate for all dataset types
         > 0: use the specified ping rate for all dataset types
        """
        assert rate is None or rate >= 0
        _LOGGER.debug("ping rate set to %d", rate)
        self._ping_rate = rate

    def update_ping_rates(self, dataset: Dict[str, Any]) -> None:
        now = datetimeutils.utcnow()

        # Filter dataset to just the ping rates
        ping_rates = { k:v for k, v in dataset.items() if k.endswith("Rate") }
        _LOGGER.debug("ping rates from dataset: %s", ping_rates)

        if self._last_updated == datetimeutils.utcmin:
            for k, v in ping_rates.items():
                self._ping_rates[k].ping_rate = v
                self._ping_rates[k].last_updated = now
        else:
            elapsed_time = now - self._last_updated
            assert len(self._ping_rates) == len(ping_rates)
            for k in self._ping_rates:
                self._ping_rates[k].ping_rate += elapsed_time.seconds
                self._ping_rates[k].last_updated = now
            _LOGGER.debug("current ping rate state: %s", self._ping_rates)

        self._last_updated = now

    def _select_ping_rate(self, body: bytes) -> int:
        assert self._ping_rate is not None
        if self._ping_rate > 0:
            ping_rate = self._ping_rate
        else:
            match = re.search(rb"<pingRate>(\d+)</pingRate>", body)
            assert match
            ping_rate = int(match.group(1))
        return ping_rate

    def update_service_ping_rates(self, dataset: Dict[str, Any]) -> None:
        # Extract ping rates from status response dataset and cache them
        ping_rates = { k:v for k, v in dataset.items() if k.endswith("Rate") }
        self._service_ping_rates = ping_rates.copy()
        _LOGGER.debug("updated service ping rates: %s", self._service_ping_rates)

    async def replace_response_ping_rates(self, response: HttpResponse) -> None:
        # assert result.type == DataSetType.PingRates
        if self._ping_rate is None:
            return

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

        _LOGGER.info("overriding ping rate to %d", ping_rate)
        _LOGGER.debug("body before replacements (%d bytes): %s", len(body), body)
        body = re.sub(rb"([pP]ingRate)>(\d+)</", rf"\1>{ping_rate}</".encode(), body)
        _LOGGER.debug("body after replacements (%d bytes): %s", len(body), body)
        response.set_body(body)

    def get_action_for_dataset(self, dataset_type: DataSetType) -> ProxyServerAction:
        ping_rate_type = self._dataset_type_map.get(dataset_type, None)
        _LOGGER.debug("ping_rate_type: %s (%s)", ping_rate_type,
            "present" if ping_rate_type in self._ping_rates else "missing")

        if ping_rate_type in self._ping_rates:
            # Consider that it may have been a while since we last updated
            service_ping_rate = -1
            if ping_rate_type in self._service_ping_rates:
                service_ping_rate = self._service_ping_rates[ping_rate_type]

            entry = self._ping_rates[ping_rate_type]
            elapsed = datetimeutils.utcnow() - entry.last_updated
            current_ping_rate = entry.ping_rate + elapsed.seconds
            _LOGGER.debug("ping rate for %s: %d sec (service: %d sec)",
                dataset_type.name, current_ping_rate, service_ping_rate)
            if current_ping_rate < service_ping_rate:
                _LOGGER.debug("suppressing server call due to unexpired timeout")
                return ProxyServerAction.Suppress

        return ProxyServerAction.Forward

    def reset_ping_rate_for_dataset(self, dataset_type: DataSetType) -> None:
        ping_rate_type = self._dataset_type_map.get(dataset_type, None)
        if ping_rate_type in self._ping_rates:
            _LOGGER.info("resetting ping rate for %s", ping_rate_type)
            self._ping_rates[ping_rate_type].ping_rate = 0
