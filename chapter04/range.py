#!/usr/bin/env python3
print("range simple example.")

r=range(10)
print(r,type(r))

l=list(r)
print(l,type(l))


r=range(0,10,3)
print(r,list(r))

for i in range(1,10,2):
    print(i)
else:
    print("last element:",i)

