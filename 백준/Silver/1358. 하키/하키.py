W,H,X,Y,P=map(int,input().split())

ans=0

def check(a,b):
    global ans

    if X<=a<=X+W and Y<=b<=Y+H:
        ans+=1
    elif ((X-a)**2+(Y+H//2-b)**2)**0.5<=H//2:
        ans+=1
    elif ((X+W-a)**2+(Y+H//2-b)**2)**0.5<=H//2:
        ans+=1

for _ in range(P):
    a,b=map(int,input().split())

    check(a,b)

print(ans)