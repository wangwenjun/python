def fun(*var):
    print(var)
    print(type(var))
    print("*"*100)
    for v in var:
        print(v)

fun(1,2,3,4,5,6,7)

print("*"*100)
fun(1,2,3,4,5,6,7,"a")
