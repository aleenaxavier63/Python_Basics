from itertools import count

#input_data="my name is aleena"
#i=0
#to count vowels in your sentence
#count=0
#length=len(input_data)
#while i<length:
 #   if input_data[i]=="a" or input_data[i]=="e" or input_data[i]=="i" or input_data[i]=="o" or input_data[i]=="u":
        #statement of if block
  #      count=count+1
   # i=i+1
#print(count)



input_data="my name is aleena"
i=0
#to count vowels in your sentence
count=0
length=len(input_data)
while i<length:
    if input_data[i]=="a" or input_data[i]=="e" or input_data[i]=="i" or input_data[i]=="o" or input_data[i]=="u":
        #statement of if block
        count=count+1
    i=i+1
#if while condition dosnot meet that condition can handle for once using else block
else:
    print("execution is completed")

print(count)



