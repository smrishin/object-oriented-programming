from abc import ABC
from enum import Enum

class VehicleSize(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"

class Vehicle(ABC):
    def __init__(self, liscense_no: str, size: VehicleSize) -> None:
        self.liscense_no = liscense_no
        self.size = size

    def get_liscense_no(self) -> str:
        return self.liscense_no
    
    def get_size(self) -> VehicleSize:
        return self.size
    
class Bike(Vehicle):
    def __init__(self, liscense_no: str) -> None:
        super().__init__(liscense_no, VehicleSize.SMALL)

class Car(Vehicle):
    def __init__(self, liscense_no: str) -> None:
        super().__init__(liscense_no, VehicleSize.MEDIUM)

class Truck(Vehicle):
    def __init__(self, liscense_no: str) -> None:
        super().__init__(liscense_no, VehicleSize.LARGE)