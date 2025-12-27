import threading
from typing import List, Dict, Optional

from entities.parkingspot import ParkingSpot
from entities.vehicle import Vehicle
from entities.parkingticket import ParkingTicket

class ParkingLot:
    _instance = None
    _lock = threading.Lock()

    def __init__(self) -> None:
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton, 1 instance already exists, cannot create another one")
        
        self.active_tickets: Dict[str, ParkingTicket] = {}
        self.spots: Dict[str, ParkingSpot] = {}
        self._main_lock = threading.Lock()

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.get_spot_id()] = spot

    def find_spot(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        available_spots = [
            spot for spot in self.spots.values()
            if not spot.is_occupied_spot() and spot.can_fit_vehicle(vehicle)
            ]
        if available_spots:
            # available_spots.sort(key=lambda x: x.get_spot_size().value)
            return available_spots[0]
        return None

    def park_vehicle(self, vehicle: Vehicle):
        with self._main_lock:
            spot = self.find_spot(vehicle)
            if spot is not None:
                spot.park_vehicle(vehicle)
                ticket = ParkingTicket(spot, vehicle)
                self.active_tickets[vehicle.get_liscense_no()] = ticket
                print(f"Vehicle {vehicle.get_liscense_no()} is parked in {spot.get_spot_id()}")
                return ticket
            else:
                print(f"No spots available")
                return None
    
    def unpark_vehicle(self, liscense_no: str):
        with self._main_lock:
            ticket = self.active_tickets.pop(liscense_no, None)
            if ticket is None:
                print(f"Invalid Ticket")
                return None
            
            ticket.set_time_out()
            spot = ticket.get_parking_spot()
            vehicle = ticket.get_vehicle()
            fees = ticket.calculate_fee()
            spot.unpark_vehicle()

            print(f"The fee for you vehicle with liscense no {vehicle.get_liscense_no()}: {fees}")

            return fees
        

