a,b=map(int,input().split())

if round(a*(1-0.01*b),6)>=100:
    print(0)
else:
    print(1)