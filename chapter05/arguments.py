def fun1(a,b):
    return a+b

def fun2(a,b=100):
    return a+b

print(fun1(1,2))
print(fun1(b=10,a=1))

print("*"*50)

print(fun2(10))
print(fun2(10,10))

