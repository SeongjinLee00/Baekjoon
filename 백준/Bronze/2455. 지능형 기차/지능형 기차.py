ans=0

tmp=0

for _ in range(4):
    a,b=map(int,input().split())

    tmp+=b
    tmp-=a

    ans=max(ans,tmp)

print(ans)