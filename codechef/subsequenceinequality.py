#!/usr/bin/env python3
n=int(input())
for i in range(0,n):
    flag=0
    temp=input()
    for i in range(0,len(temp)):
        for j in range(i+1,len(temp)):
            if temp[i]==temp[j]:
                flag=1
    if flag==0:
        print("no")
    else:
        print("yes")