#!/usr/bin/env python3
n=int(input())
listx=[]
sumx=[int(0)]*n
k=0
for i in range(0,n):
    listx.append(input().split())
for i in range(0,n):
    for j in range(0,n):
        sumx[k]=sumx[k]+listx[i][j]
    k+=1
print(listx)
print(sumx)