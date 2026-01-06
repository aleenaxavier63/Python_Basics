class Home:
    def __init__(self):
        self.__address="koodely"#private attribute
    def get_address(self):
        return self.__address
    def set_address(self, new_address):
        self.__address=new_address

h=Home()
#no accesibilty outside class-so will get error-'Home' object has no attribute '__address'.so use getters and setters method
#print(h.__address)
# so when use getter and setter method
h.set_address("kool")
print(h.get_address())