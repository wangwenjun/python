list=[1,2,3,4,5]

print(list)
list.remove(2)
print(list)

# the remove element is not exist will throw error.
#Traceback (most recent call last):
#  File "list-remove.py", line 8, in <module>
#    list.remove(100)
#ValueError: list.remove(x): x not in list

#list.remove(100)
#print(list)


#so how to remove the element maybe not exist in list???

e=100
if e not in list:
    print(f"The element {e} not in list {list} at all.")
else:
    list.remove(e)
    print(list)
