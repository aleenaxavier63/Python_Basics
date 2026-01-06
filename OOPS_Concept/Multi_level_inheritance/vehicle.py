class Vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def display(self):
        print("model is:",self.model)
        print("year is:",self.year)
