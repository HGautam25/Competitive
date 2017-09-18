#!/usr/bin/env python3
candles=int(input())
n=[int(i) for i in input().split(' ')]
maxn=max(n)
print(n.count(maxn))