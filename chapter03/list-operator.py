#!/usr/bin/env python3

digits=[1,2,3,4,5,6,7,8]

#print the list and length of list
print(id(digits),digits,"len=",len(digits))

digits[2]="AlexWang"
print(id(digits),digits,"len=",len(digits))

##############################append the new element into list
digits.append("Hello")
digits.append(122)
print(id(digits),digits,"len=",len(digits))
##############################update the element by batch, actually is depend on  the slice operator

digits[2:5]=["a","b","c"]
print(id(digits),digits,"len=",len(digits))

