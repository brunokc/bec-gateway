from datetime import datetime
from .handlermaps import DataSetType

class DataSet:
    def __init__(self):
        self.lastUpdated = datetime.min
        self.data = { }

    def update(self, dataset):
        self.data.update(dataset)
        self.lastUpdated = datetime.now()

    def __str__(self):
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


    def update(self, dataset_type, newdataset):
        dataset = self._dataset_type_map.get(dataset_type)
        if dataset:
            dataset.update(newdataset)
