#!/usr/bin/env python3
numbers=[[1,2,3],[4,5,6],[7,8,9]]
print("before numbers:",numbers)
for i in range(0,len(numbers)):
    for j in range(0,len(numbers[i])):
        v=numbers[i][j]
        numbers[i][j]=v**2

print("after numbers:",numbers)
