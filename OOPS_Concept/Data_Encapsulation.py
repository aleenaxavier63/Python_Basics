class Person:
    def __init__(self,name,age,password):
        #no underscore-public visibility mode-every file in same package or outside package can access this age
        self.name=name
        #single underscore-protected variable using getter method or using objects by using single underscore
        self._age=age
        #double underscore--private-can access using getter and setter method-data encapsulation needed
        self.__password=password

    def get_password(self):
        #to retreive data
        return self.__password
    def set_password(self,password):
        #to set data(updation)
        self.__password=password

# this password attribute in get and set
#getter and setter method are related

