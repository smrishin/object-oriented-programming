from parkinglot import ParkingLot
from entities.parkingspot import ParkingSpot
from entities.parkingticket import ParkingTicket
from entities.vehicle import Bike, Car, Truck, Vehicle, VehicleSize


class Demo:
    @staticmethod
    def main():
        # create a single parking lot instance
        PL = ParkingLot.get_instance()

        # create vehicles
        gaadi1 = Bike("abc")
        gaadi2 = Bike("xyz")

        car1 = Car("A9A")
        car2 = Car("8CM")

        lorry1 = Truck("qwe")
        lorry2 = Truck("rty")

        # create parking spots
        PL.add_spot(ParkingSpot("1", VehicleSize.SMALL))
        PL.add_spot(ParkingSpot("2", VehicleSize.SMALL))
        PL.add_spot(ParkingSpot("3", VehicleSize.SMALL))
        PL.add_spot(ParkingSpot("4", VehicleSize.MEDIUM))
        PL.add_spot(ParkingSpot("5", VehicleSize.MEDIUM))
        PL.add_spot(ParkingSpot("6", VehicleSize.LARGE))

        # Park all vehciles
        gaadi1_t = PL.park_vehicle(gaadi1)
        gaadi2_t = PL.park_vehicle(gaadi2)
        car1_t = PL.park_vehicle(car1)
        car2_t = PL.park_vehicle(car2)
        lorry1_t = PL.park_vehicle(lorry1)
        lorry2_t = PL.park_vehicle(lorry2) # spot will not be available

        # unpark and park new vehicle in the same spot
        lorry1_fee = PL.unpark_vehicle(lorry1.get_liscense_no())
        lorry2_t = PL.park_vehicle(lorry2)

        # unpark all vehicles
        gaadi1_fee = PL.unpark_vehicle(gaadi1.get_liscense_no())
        gaadi2_fee = PL.unpark_vehicle(gaadi2.get_liscense_no())
        car1_fee = PL.unpark_vehicle(car1.get_liscense_no())
        car2_fee = PL.unpark_vehicle(car2.get_liscense_no())
        lorry2_fee = PL.unpark_vehicle(lorry2.get_liscense_no())

        # try to unpark vehicle which was already unparked, Invalid case
        lorry1_fee = PL.unpark_vehicle(lorry1.get_liscense_no())




if __name__ == "__main__":
    Demo.main()