#!/usr/bin/env python3
digits=[1,2,3,4,5,6,7,8]
print(digits,"len=",len(digits))

print(digits[1])

for i in range(0,len(digits)):
    print(digits[i])

print("*"*10)
tmp=len(digits)-1
len=len(digits)
while tmp>=0:
    print(digits[tmp-len])
    tmp-=1
