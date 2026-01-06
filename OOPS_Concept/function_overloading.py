class Greet:
    def greeting(self,name=None):
        #can pass 0 or 1 value as name=None.#we can write this any number of times.for each we should provide conditions
        if name:
            print("hello "+name)
        else:
            print("hello")
g1=Greet()
#will work with or without argument
#if there is change in parameter or return type, and this same will apply on same
g1.greeting("aleena")
#if part will work for above
g1.greeting()
#else part works for above
#here we change number of parameters
#this is function overloading or compile time polymorphism
#java we cannot use same variable 2 times
#in java same method name with diff para
#but in python same method name diff arg does not work.why?


#we have variable length()-we can achieve function overloading
#either function with default value or using variable length function