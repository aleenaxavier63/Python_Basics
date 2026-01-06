a=int(input("Enter a number:"))
#if
if a>=18:
    print("Age is greater than 18")
#if else
if a>=18:
    print("Age is greater than 18")
else:
    print("Age is less than or equal to 18")
#if elif
if a<=13:
    print("child")
elif (a>13) and (a<=17):
    print("teenager")
else:
    print("adult")

#read an operation if it is +-do addition, - subtraction, ....

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))
x=input("Enter the operation:")
if x=="Addition":
    print(num1+num2)
elif x=="Subtraction":
    print(num1-num2)
elif x=="multiplication":
    print(num1*num2)
elif x=="Division":
    print(num1/num2)
else:
    print('Invalid Operation')