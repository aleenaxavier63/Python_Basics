from OOPS_Concept.Multiple_inheritance.Father import Father
from OOPS_Concept.Multiple_inheritance.Mother import Mother

#passing both parent into child
class Child(Father,Mother):

    def skills(self):

        super().skills()
        #polymorphism#exceute either father or mother.order of which will excecute.the one which execute first override the first one and overwrite it
        print("Child paints")

c1=Child()
c1.skills()

#we have 2 parent class.mother and father has same name method.skill,so method present in father override by mother.(important question-if if child and parent had same method name,how it will execute)
# which one invoke first -no order.each time execution we may get iff output.
#hoe it works:-when child class check this function-it will see super().skills()->2 parents-there is no order which will execute.either father or mother.
#which on eis execute first that class will override first class and overwrite it-kind of polymorphism