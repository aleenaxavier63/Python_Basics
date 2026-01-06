class Student:
    school_name="ABC"#class variable acessed by class name
    def __init__(self,name,age):
        print("this is a constructor")
        #to pass attributes
        self.name=name
        self.age=age

    def display(self):
        print(self.name,self.age)
        print("school name is ",Student.school_name)

student1=Student("Aleena",20)
student1.display()
student2=Student("Milna",30)
student2.display()
