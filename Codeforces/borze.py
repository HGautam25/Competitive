#!/usr/bin/env python3
str1=input()
i=0
while (i < len(str1)):
    if(str1[i]=='.'):
        print(0,end='')
        i+=1
    elif(str1[i]=='-'):
        if(str1[i+1]=='.'):
            print(1,end='')
            i+=2
        else:
            print(2,end='')
            i+=2
    else:
        pass
