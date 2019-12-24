def negative(a):
    return -a

list=[345,435,23,34,12,56,1]
print(list)
list.sort()
print(list)
print("*"*100)

list.sort(reverse=True)
print(list)
print("*"*100)

list.sort(key=negative)
print(list)
print("*"*100)

