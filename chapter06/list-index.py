list=[1,2,3,4,5,3,7,8,3]
print(list)

#index=3
print(list.index(4))
#index=2
print(list.index(3))

#include the start index
print(list.index(3,2))

#Traceback (most recent call last):
#  File "list-index.py", line 12, in <module>
#    print(list.index(3,3,5))
#ValueError: 3 is not in list
#exclude the end index
#print(list.index(3,3,5))

