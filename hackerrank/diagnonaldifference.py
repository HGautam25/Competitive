#!/usr/bin/env python3
n=int(input())
# list1=[[int(input().split(' ')) for i in range(0,n)]for j in range(0,n)]
arr2d = [[j for j in input().strip()] for i in range(n)]
print(arr2d)