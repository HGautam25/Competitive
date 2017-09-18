#!usr/bin/env python3
n=int(input())
countp,countn,countz,count=0,0,0,0
list1=[int(j) for j in input().split(' ')]
for temp in list1:
    if temp<0:
        countn+=1
        count+=1
    elif temp>0:
        countp+=1
        count+=1
    else:
        countz+=1
        count+=1
print(round(countp/count,6))
print(round(countn/count,6))
print(round(countz/count,6))
