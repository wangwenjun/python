#!/usr/bin/env python3
release_year=1991
answer=int(input("please input the python release year:"))
if answer==release_year:
    print("correctly. you are right!")
elif answer>release_year:
    print(f"{answer} is too late.")
elif answer<release_year:
    print(f"{answer} is too early.")

print("Bye!")
