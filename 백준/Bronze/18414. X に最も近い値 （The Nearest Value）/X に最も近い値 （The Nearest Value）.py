x,l,r=map(int,input().split())

if l<=x<=r:
    print(x)
elif abs(l-x)>abs(r-x):
    print(r)
else:
    print(l)