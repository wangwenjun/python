#!/usr/bin/env python3
while 1:
    str=input("please enter the string:")
    if str=="quit":
        break
    else:
        strLen=len(str)
        lastNum=int(input("How many last letters should be converted?"))
        result=""
        if lastNum>strLen:
            result=str.upper()
        elif lastNum<0:
            result=str
        else:
            firstHalfOfStr=str[:strLen-lastNum]
            secondHalfOfStr=str[strLen-lastNum:]
            result=firstHalfOfStr+secondHalfOfStr.upper()
        print(f"convert result is {result}")
