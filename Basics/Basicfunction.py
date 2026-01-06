from OOPS_Concept.Data_Encapsulation import Person


def add():
    #function defenition
    a=2
    b=3
    print(a+b)
#to invoke function
add()
add()

#parameterized function
def add1(c,d):
    print(c+d)

add1(2,7)
add1(4,2)

#parameterized function with return value

def addition(a,b):
    return a+b
var1=addition(9,4)
print(var1)

#basic function with return value

def addition1():
    a=4
    b=6
    return a+b

var3=addition1()
print(var3)

#perform subtraction,by taking input from outside
def subtraction(c,d):
    return c-d
var4=subtraction(5,4)
print(var4)

# to print result of add,sub,mul and duv
#multiple return values
def perform_calc(a,b):
    return a+b,a-b,a*b,a/b

var5,var6,var7,var8=perform_calc(5,4)

print(var5,var6,var7,var8)

#variable length function
#max(),min() all are built in function
def findMax(*args):
    return(max(args))

maximun=findMax(10,20,60)
print(maximun)
maximun1=findMax(10,20,60,80)
print(maximun1)
maximun2=findMax(10,20)
print(maximun2)

#anonymous funtion
add4=lambda x,y:x+y
print(add4(20,10))

p=Person("aleena",2,"aa")
#name-public attribute, so can access
p.name="ann"
print(p.name)
#age is protected-so access using undescore-can acessible from different packages too-why-because of__init()-so it accessible from different
#package in python
#if not __init function-we cannot access age
print(p._age)









