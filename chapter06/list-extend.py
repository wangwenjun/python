list=[1,2,3,4,5]
print(id(list),list)
list.extend([3,4,5,6])
print(id(list),list)
list.extend("Hello World")
print(id(list),list)
