from OOPS_Concept.Heirarchical_inheritance.Vehicle import Vehicle1



class Car(Vehicle1):
    def vehicle_details(self):
        print("Car is a 4 wheeler")

c=Car()
c.vehicle_details()
c.vehicle_features()

