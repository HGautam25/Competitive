#!/usr/bin/env python3
a0,a1,a2=input().strip().split(' ')
a0,a1,a2=int(a0),int(a1),int(a2)
b0,b1,b2=input().strip().split(' ')
b0,b1,b2=int(b0),int(b1),int(b2)
a,b=0,0
if a0<b0:
    b+=1
elif a0>b0:
    a+=1
else:
    pass

if a1<b1:
    b+=1
elif a1>b1:
    a+=1
else:
    pass

if a2<b2:
    b+=1
elif a2>b2:
    a+=1
else:
    pass
print(a,b)