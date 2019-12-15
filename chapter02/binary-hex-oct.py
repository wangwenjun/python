#!/usr/bin/env python3
b=0b11
print(type(b),b)

b=0b110
print(type(b),b)

x=0xfff
print(type(x),x)

o=0o20
print(type(o),o)


b=bin(123)
print(b,type(b))

h=hex(425)
print(h,type(h))

o=oct(24234)
print(o,type(o))

number=input("Convert to binary:")
print(int(number))

print(bin(int(number)))
print(hex(int(number)))
print(oct(int(number)))

