from datetime import datetime
from typing import Any, Dict
from .handlermaps import DataSetType

class DataSet:
    def __init__(self) -> None:
        self.lastUpdated = datetime.min
        self.data: Dict[str, Any] = { }

    def update(self, dataset: Dict[str, Any]) -> None:
        self.data.update(dataset)
        self.lastUpdated = datetime.now()

    def __str__(self) -> str:
        return "\n".join([f"{k}={v}" for k, v in self.data.items()])


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
        dataset = self._dataset_type_map.get(dataset_type)
        if dataset:
            dataset.update(newdataset)
