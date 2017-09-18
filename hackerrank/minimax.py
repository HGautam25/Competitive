#!/usr/bin/env python3
"""Combinations possible : for 5 is 5C4: 5"""
n=[int(j) for j in input().split(' ')]
minsum=0
maxsum=0
minsum=sum(n)-max(n)
maxsum=sum(n)-min(n)
print(minsum,maxsum)