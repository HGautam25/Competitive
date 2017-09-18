#!/usr/bin/env python3
n=int(input())
for i in range(n-1,-1,-1):
    for j in range(i,0,-1):
        print(" ",end='')
    for k in range(i-1,n-1):
        print("#",end='')
    print("")

