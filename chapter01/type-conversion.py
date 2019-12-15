#!/usr/bin/python3.6

i=7
print(i,type(i))

i=str(i)
print(i,type(i))

i="10"
print(i,type(i))

i=int(i)
print(i,type(i))

f=533.4
print(type(f))

print(int(f))

f="3453.24"
print(float(f))


del f
#this print statement will be error due to the variable f is deleted.
#print(f)
