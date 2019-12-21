#!/usr/bin/env python3
# A while statement allows you to execute a block of code repeatedly
release_year=1991
correct=False
while not correct:
    year=int(input("please input the python first release year:"))
    if year==release_year:
        correct=True
    elif year>release_year:
        print("too late.")
    elif year<release_year:
        print("too early.")
else:
    print("Exactly. you are right!")

