class Vehicle:
    def __init__(self, name, minutes):
        self.name = name
        self.minutes = minutes

    def fare(self):
        return self.minutes * 0.25

class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare() 
        return base_fare

a = int(input("Please enter how many minutes you have been in the bus: "))
if __name__ == "__main__":
    school_bus = Bus("School Volvo",a )

    print(f"Vehicle Name: {school_bus.name}")
    print(f"Minutes spent in bus: {school_bus.minutes}")
    print(f"Total Fare: {school_bus.fare()}")