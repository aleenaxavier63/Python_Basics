#child class
from OOPS_Concept.Multi_level_inheritance.vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,color,milage,model,year):
        super().__init__(model,year) #super keyword to accuqure somthing from parent class
        self.color=color
        self.milage=milage
    def display(self): #function overriding-polymorphism concept
        super().display()
        print(self.color,self.milage)
Car1=Car("red",2000,1000,2025)
Car1.display()
