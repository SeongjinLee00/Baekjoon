a,b=map(int,input().split())

if (a+b)%2 or (a-b)%2 or b>a:
    print(-1)
    exit(0)

x,y=(a+b)//2,(a-b)//2

if x>y:
    print(x,y)
else:
    print(y,x)