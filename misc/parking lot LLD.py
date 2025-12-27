import heapq
from datetime import datetime, timedelta

class Vehicle:
    def __init__(self, vehicle_id, type):
        self.vehicle_id = vehicle_id
        self.type = type

class ParkingSpot:
    def __init__(self, spot_id, spot_size):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_available = True
        self.assinged_vehicle = None
    
    def assign_vehicle(self, vehicle: Vehicle):
        if self.is_available and self.spot_size >= vehicle.type:
            self.is_available = False
            self.assinged_vehicle = vehicle
            return True
        return False

    def unassign_vehicle(self):
        if not self.is_available:
            self.is_available = True
            vehicle = self.assinged_vehicle
            self.assinged_vehicle = None
            return vehicle
        return None

class Ticket:
    def __init__(self, ticket_id, time_in, vehicle, parking_spot):
        self.id = ticket_id
        self.time_in = time_in
        self.time_out = None
        self.vehicle = vehicle
        self.parking_spot = parking_spot
    
    def assign_time_out(self, time_out):
        self.time_out = time_out

    def calculcate_fee(self):
        if not self.time_out:
            raise Exception("Time out not set")

        duration = (self.time_out - self.time_in).total_seconds()/3600

        return round(duration * self.vehicle.type, 2)

        
class ParkingLot:
    def __init__(self, parking_spots):
        self.active_tickets = {}
        self.available_spots = []
        self.parking_map = {spot.spot_id: spot for spot in parking_spots}
        for spot in parking_spots:
            # min heap
            heapq.heappush(self.available_spots, (spot.spot_size, spot.spot_id, spot))
        
    def generate_ticket_id(self):
        return len(self.active_tickets) + 1
    
    def assign_spot(self, vehicle, time_in):
        temp_spots = []
        while self.available_spots:
            spot_size, spot_id, spot = heapq.heappop(self.available_spots)
            if spot.assign_vehicle(vehicle):
                ticket_id = self.generate_ticket_id()
                ticket = Ticket(ticket_id, time_in, vehicle, spot)
                self.active_tickets[ticket_id] = ticket

                for spot_size, spot_id, spot in temp_spots:
                    heapq.heappush(self.available_spots, (spot_size, spot_id, spot))
                return ticket_id
            else:
                temp_spots.append((spot_size, spot_id, spot))
        
        for spot_size, spot_id, spot in temp_spots:
            heapq.heappush(self.available_spots, (spot_size, spot_id, spot))

        raise Exception("Spot unavailable for your vehicle")

    
    def unassign_spot(self, ticket_id, time_out):
        ticket = self.active_tickets.get(ticket_id, None)
        if not ticket:
            raise Exception("Invalid Ticket")

        ticket.assign_time_out(time_out)
        fee = ticket.calculcate_fee()

        spot = ticket.parking_spot 
        spot.unassign_vehicle()
        heapq.heappush(self.available_spots, (spot.spot_size, spot.spot_id, spot))

        del self.active_tickets[ticket_id]

        return fee
        
    
    

car1 = Vehicle(1, 1)
car2 = Vehicle(2, 2)
car3 = Vehicle(3, 3)

spot1 = ParkingSpot(1, 1)
spot2 = ParkingSpot(2, 2)

parkingLot = ParkingLot([spot1, spot2])

in_car1 = datetime.now()
ticket = parkingLot.assign_spot(car3, in_car1) 
print(ticket)

out_car1 = in_car1 + timedelta(hours=2)
print(parkingLot.unassign_spot(ticket, out_car1))







