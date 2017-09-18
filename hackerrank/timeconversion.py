#!/usr/bin/env python3
timeampm=[j for j in input()]
temp=0
if(timeampm[8]=="A"):
    if(timeampm[0]=='1'):
            if(timeampm[1]=='2'):
                timeampm[0]='0'
                timeampm[1]='0'
    print(''.join(str(x) for x in timeampm[0:8]))
        
elif(timeampm[8]=="P"):
    temp=int(timeampm[0]*10)
    temp+=int(timeampm[1])
    temp+=12
    timeampm[0]=int(temp/10)
    timeampm[1]=temp%10
    print(timeampm[0:2])
    print(''.join(str(x) for x in timeampm[0:8]))
else:
    print(timeampm,"pass")