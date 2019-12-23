def return_value(a,b):
    return a+b

def no_return_value(a,b):
    a+b

v=return_value(1,2)
print(v,v==3)
v=no_return_value(1,2)
print(v,v==None,v is None)

