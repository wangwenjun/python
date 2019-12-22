#!/usr/bin/env python3


for i in range(1,10):
    j=1
    output=""
    while j<=i:
        if i==j:
            output+=f"{i}*{j}={i*j}"
        else:
            output+=f"{i}*{j}={i*j},"
        j+=1
    else:
        print(output)
