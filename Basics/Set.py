set1={}
print(set1)

set2={1,5,3,7,2,6}
print(set2)

list1=["aleen","anu","milna"]
set2.update(list1)
print(set2)

tuple1=(11,22,33,44,55,66)
print(tuple1)
set2.add(tuple1)
print(set2)

#print(sorted(set2))
set2.clear()
print(set2)

new_set={11,66,33,10,55,22}
print(sorted(new_set))

#frozenset
x=frozenset(new_set)
print(x)

