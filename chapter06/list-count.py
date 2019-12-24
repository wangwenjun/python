list=[1,2,3,4,5,6,5,5]

#1,3
print(list.count(1),list.count(5)) 
#list.clear === del[:]
list.clear()
print(list)

list=[1,2,3,4,5,6,5,5]
del list[:]
print(list)

list=[1,2,3,4,5,6,5,5]
print(list)
list.pop()
print(list)
del list[-1:]
print(list)
