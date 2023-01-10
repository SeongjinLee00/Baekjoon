n=int(input())

ans=0

for _ in range(n):
    a,b=input().split('-')
    
    if int(b)<=90:
        ans+=1

print(ans)