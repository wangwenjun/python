for i in range(1,11):
    print(i)

print("*"*100)


l=[i for i in range(1,11)]
print(l)

print("*"*100)
l=list(range(1,11))
print(l)


l=list(i*10 for i in range(1,11))
print(l)

l=[i for i in range(1,11) if i%2==0]
print(l)
