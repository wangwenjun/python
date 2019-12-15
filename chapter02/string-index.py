#!/usr/bin/env python3

str="Python is fun"
print(str,"length is:",len(str))

for i in range(0,len(str)):
    print("Index[",i,"]=",str[i])

print("*"*100)

for i in range(-len(str),0):
    print("Index[",i,"]=",str[i])

s="Hello World"
#index out of range
#print(s[100])


