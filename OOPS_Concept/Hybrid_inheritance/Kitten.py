from OOPS_Concept.Hybrid_inheritance.Animal import Animal
from OOPS_Concept.Hybrid_inheritance.Cat import Cat
from OOPS_Concept.Hybrid_inheritance.cat1 import Cat1


class Kitten(Animal,Cat1):
    def kitten_ability(self):
        super().cat1abilty()
        print("kitten sound")

kitten=Kitten()
kitten.kitten_ability()
