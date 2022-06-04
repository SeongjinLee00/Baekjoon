from collections import defaultdict

xdic=defaultdict(int)
ydic=defaultdict(int)

for _ in range(3):
    x,y=map(int,input().split())

    xdic[x]+=1
    ydic[y]+=1

for k,v in xdic.items():
    if v==1:
        xans=k

for k,v in ydic.items():
    if v==1:
        yans=k

print(xans,yans)