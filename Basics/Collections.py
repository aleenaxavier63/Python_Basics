list1=[1,'aleena',2.5]
print(list1)

#to print [5,5,5,5,5......]
rep_list=[5]*10
print(rep_list)

print(list1[0])
print(list1[-1])

#add a new value to the second index value
list1.insert(2,'z')
print(list1)
list1.append(6)
print(list1)

#accesing index by value
print(list1.index(2.5))
#print(list1.index("hai"))

list2=[2,6,3,21]
list2.sort()
print(list2)
#here revesring sorted list2
# so to get in descending order.Sort first, then reverse
list2=[2,6,3,21]
list2.reverse()
print(list2)

print(list2.count(6))
print(list2.count('p'))
