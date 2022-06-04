T=int(input())

for _ in range(T):
    x1,y1,x2,y2=map(int,input().split())

    N=int(input())
    ans=0

    for _ in range(N):
        cx,cy,r=map(int,input().split())
        if ((cy-y1)**2+(cx-x1)**2)**0.5<r and ((cy-y2)**2+(cx-x2)**2)**0.5<r:
            continue
        elif ((cy-y1)**2+(cx-x1)**2)**0.5<r:
            ans+=1
        elif ((cy-y2)**2+(cx-x2)**2)**0.5<r:
            ans+=1

    print(ans)