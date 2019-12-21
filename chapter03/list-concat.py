#!/usr/bin/env python3

digits=[1,2,3,4,5,6,7,8]

#print the list and length of list
print(digits,"len=",len(digits))

print(id(digits))
digits+=[9,10,11]

print(id(digits))

print(digits)

