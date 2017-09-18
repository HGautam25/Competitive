#!usr/bin/env python3
# year=int(input())
# tempyear=year
def isuniq(n):
    xor=n%10
    while n>0:
        n=int(n/10)
        xor^=n
        print(xor,n)
    return xor
print(isuniq(1234))
print(isuniq(1123))
