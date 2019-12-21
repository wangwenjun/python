#!/usr/bin/env python3
print("for loop the string")
str="Hello World."
for s in str:
    print(s,s.upper())

print("*"*100)

list=[1,2,3,4,5,6,7,8,9]
for e in list:
    print(e,"square is:",e**2)

print("*"*100)

for e in (1,2,3,4,5):
    print(e,"pow 3:",pow(e,3))
