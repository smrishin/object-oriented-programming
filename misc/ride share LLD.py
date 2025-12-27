from collections import defaultdict

class User:
    def __init__(self, user_id, loc):
        self.id = user_id
        self.loc = loc

class Driver(User):
    pass

class Rider(User):
    pass

class Trip:
    def __init__(self, trip_id, rider: Rider, driver: Driver, source, destination):
        self.id = trip_id
        self.rider = rider
        self.driver = driver
        self.status = "requested"
        self.source = source
        self.destination = destination

    def start_trip(self):
        if self.status != "requested":
            raise Exception("Trip not requested")
        self.status = "in progress"

    def end_trip(self):
        if self.status != "in progress":
            raise Exception("Trip not in progress")
        self.status = "completed"

    def calculate_price(self):
        distance = self.destination - self.source
        price = round(distance * 2, 2)
        return price
        
        

class RideShare:
    def __init__(self):
        self.available_drivers = defaultdict(Driver)
        self.available_riders = defaultdict(Rider)
        self.active_trips = defaultdict(Trip)

    def driver_signup(self, loc):
        # return driver id
        driver_id = len(self.available_drivers) + 1
        driver = Driver(driver_id, loc)
        self.available_drivers[driver_id] = driver
        return driver_id

    def rider_signup(self, loc):
        # return rider_id
        rider_id = len(self.available_riders) + 1
        rider = Rider(rider_id, loc)
        self.available_riders[rider_id] = rider
        return rider_id

    def find_available_drivers(self, source):
        # return driver
        closest_driver = None
        min_distance = float("inf")
        for driver_id, driver in self.available_drivers.items():
            distance = abs(driver.loc - source)
            if distance < min_distance:
                min_distance = distance
                closest_driver = driver
                
        return closest_driver

    def request_ride(self, rider_id, destination):
        rider = self.available_riders.get(rider_id, None)
        if not rider:
            raise Exception("Invalid Rider")
        
        source = rider.loc

        driver = self.find_available_drivers(source)            
        if not driver:
            raise Exception("Driver not found")
        
        trip_id = len(self.active_trips) + 1
        new_trip = Trip(trip_id, rider, driver, source, destination)
        self.active_trips[trip_id] = new_trip

        new_trip.start_trip()
        print(f"Driver {driver.id} is picking up rider {rider.id} from {source}")

        del self.available_drivers[driver.id]
        # if rider is not allowed to do multiple rides at the same time
        del self.available_riders[rider_id]

        return trip_id
    
    def end_ride(self, trip_id):
        trip = self.active_trips.get(trip_id, None)
        if not trip:
            raise Exception("Invalid Trip Id")
        
        trip.end_trip()
        price = trip.calculate_price()

        self.available_drivers[trip.driver.id] = trip.driver
        self.available_riders[trip.rider.id] = trip.rider

        trip.driver.loc = trip.rider.loc = trip.destination

        del self.active_trips[trip_id]
        print(trip.driver.loc)
        return price
        # return price

    def get_ride_status(self, trip_id):
        # returns trip status
        trip = self.active_trips.get(trip_id, None)
        if not trip:
            raise Exception("Invalid Trip id")
        
        return trip.status
        # pass


system = RideShare()

d1 = system.driver_signup(5)
d2 = system.driver_signup(8)
print(f"Drivers {d1} {d2}")

r1 = system.rider_signup(0)
print(f"Riders {r1}")

t1 = system.request_ride(r1, 15)
print(f"Trip for {r1} is {t1}")

print("Trip status: ", system.get_ride_status(t1))

price = system.end_ride(t1)

print(f"price is {price}")

# print(d1.loc)