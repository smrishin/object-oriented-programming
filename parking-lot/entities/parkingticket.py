import uuid
import time
from enum import Enum
from entities.vehicle import Vehicle, VehicleSize
from entities.parkingspot import ParkingSpot

HOURLY_RATES = {
    VehicleSize.SMALL: 10.0,
    VehicleSize.MEDIUM: 20.0,
    VehicleSize.LARGE: 30.0
    }

class ParkingTicket:
    def __init__(self, parking_spot: ParkingSpot, vehicle: Vehicle) -> None:
        self.ticket_id = str(uuid.uuid4())
        self.parking_spot = parking_spot
        self.vehicle = vehicle
        self.time_in = int(time.time() * 1000)
        self.time_out = 0
    
    def get_ticket_id(self) -> str:
        return self.ticket_id
    
    def get_vehicle(self) -> Vehicle:
        return self.vehicle
    
    def get_parking_spot(self) -> ParkingSpot:
        return self.parking_spot
    
    def get_time_in(self) -> int:
        return self.time_in
    
    def get_time_out(self) -> int:
        return self.time_out
    
    def set_time_out(self) -> None:
        self.time_out = int(time.time() * 1000)

    def calculate_fee(self) -> float:
        duration = self.time_out - self.time_in
        hours  = (duration//(1000*60*60)) + 1
        return hours * HOURLY_RATES[self.vehicle.get_size()]
        
