from OOPS_Concept.Multi_level_inheritance.Bike import Bike


class Motorbike(Bike):
    def __init__(self, brand, model,year,color):
        super().__init__(brand,model,year)
        self.color = color

    def display(self):
        super().display()
        print("color is:",self.color)

motorbike1=Motorbike("Benz",200,2012,"red")
motorbike1.display()
