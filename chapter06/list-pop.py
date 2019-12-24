list=[1,2,3,4,5,6]

print(list)
pop=list.pop()
print(pop==6,list)
print("*"*100)

pop=list.pop(3)
print(pop==4,list)
print("*"*100)

#Traceback (most recent call last):
#  File "list-pop.py", line 12, in <module>
#    pop=list.pop(100)
#IndexError: pop index out of range
#
#pop=list.pop(100)
#print(pop,list)
