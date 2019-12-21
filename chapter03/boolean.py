#!/usr/bin/env python3
b=True
print(b,type(b),id(b))

b=1<10
print(b,type(b),id(b))

b=10>100
print(b,type(b),id(b))

s1="Hello"
s2="Hello"
s11=s1
s22=s2
print(s1==s2)
print(s1==s11)
print(s1 is s11)
print(s1 is s2)

s3="3453453"
print(s3 is not None)
s3=None
print(s3 is not None)
print(s3 is None)


str="Hello World"
print("H" in str)
