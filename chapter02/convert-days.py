#!/usr/bin/env python3
days=int(input("please enter the days:"))

years=days//365
print("Years:",years)

weeks=(days-years*365)//7
print("Weeks:",weeks)
print("Days:",(days-years*365-weeks*7))

