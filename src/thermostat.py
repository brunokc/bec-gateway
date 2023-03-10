from datetime import datetime, timezone
from typing import Any, Dict
from .handlermaps import DataSetType

from . import jsonutils

class DataSet:
    def __init__(self) -> None:
        self.last_updated = datetime.min
        self.data: Dict[str, Any] = { }

    def __len__(self) -> int:
        return len(self.data)

    def update(self, dataset: Dict[str, Any]) -> None:
        self.data.update(dataset)
        self.last_updated = datetime.now(timezone.utc)

    def __str__(self) -> str:
        # return "\n".join([f"{k}={v}" for k, v in self.data.items()])
        return jsonutils.dumps(self.data, indent=2)


class ConnexThermostat:
    def __init__(self, serial_number: str):
        self.serial_number = serial_number
        self.status: DataSet = DataSet()
        self.idustatus: DataSet = DataSet()
        self.odustatus: DataSet = DataSet()
        self.ping_rates: DataSet = DataSet()

        self._dataset_type_map = {
            DataSetType.Status: self.status,
            DataSetType.IduStatus: self.idustatus,
            DataSetType.OduStatus: self.odustatus,
            DataSetType.PingRates: self.ping_rates,
        }

    def update(self, dataset_type: DataSetType, newdataset: Dict[str, Any]) -> None:
        dataset = self._dataset_type_map.get(dataset_type, None)
        if dataset is not None:
            dataset.update(newdataset)
