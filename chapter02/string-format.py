#!/usr/bin/env python3

import math

str=f"math.pi={math.pi}"
print(str)

name="Alex"

str=f"{name} learning python and {name} length is:{len(name)}"

print(type(str))
print(str)


i=10
print(f"i equal {i} and add 10 equal to {i+10}")

str="{} learning python and {} length is:{}"
print(str.format(name,name,len(name)))
x=10
y=20
print("{}+{}={}".format(x,y,x+y))

print("%d+%d=%d"%(x,y,x+y))
