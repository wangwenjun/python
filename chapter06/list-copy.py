list=[1,2,3,4,5,6]

#deep clone
list2=list.copy()
print(id(list),list,id(list2),list2)
print("*"*100)


list.insert(3,100)
print(id(list),list,id(list2),list2)
print("*"*100)

list.clear()
print(id(list),list,id(list2),list2)
print("*"*100)

