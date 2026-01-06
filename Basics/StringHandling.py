message="this is sample"
print (message[0])
print (message[-1])
print(message[-4])
length=len(message)
for i in range(length):
    print(message[i])

print(message[1:5])
print(message[:5])
print(message[5:])

#to concatenate hello before message
Greeting="hello "+message
print(Greeting)

print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())

#searching
print("this" in message)
print("That" in message)

new_message=message.replace("this","that")
print(new_message)

