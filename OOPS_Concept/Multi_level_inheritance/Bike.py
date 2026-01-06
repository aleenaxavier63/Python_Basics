class Bike(Vehicle):
    def vehicle_details(self):
        super().vehicle_details()
        print("Bike is a 2 wheeler Vehicle ")

bike = Bike()
bike.vehicle_details()
bike.vehicle_features()