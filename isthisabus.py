class vehicle:

    def __init__(self, name, max, mileage):
        self.name = name
        self.maxspeed = max
        self.mileage = mileage

class Bus(vehicle):
    pass

School_bus = Bus("School Volvo","190", "10")
print("Vehicle name:",School_bus.name,"\n","Speed:", School_bus.maxspeed,"\n", "Mileage:", School_bus.mileage)

    