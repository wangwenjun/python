#!/usr/bin/env python3
l1=[1,2,3]
l2=l1
print(l1,l2,id(l1),id(l2))

l2[2]=30
print(l1,l2,id(l1),id(l2))

print("*"*100)
str="HelloWorld"
str1=str
print(str,str1,id(str),id(str1))

str1+="X"
print(str,str1,id(str),id(str1))
