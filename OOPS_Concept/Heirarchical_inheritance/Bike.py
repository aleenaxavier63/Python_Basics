from OOPS_Concept.Heirarchical_inheritance.Vehicle import Vehicle1


class Bike(Vehicle1):
    def vehicle_details(self):
        print("Bike has 2 wheels")

b=Bike()
b.vehicle_details()
b.vehicle_features()
