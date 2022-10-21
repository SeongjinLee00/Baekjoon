import math

N=int(input())
numbers=list(map(int,input().split()))
a,b=map(int,input().split())

ans=0

for num in numbers:
    if num-a>0:
        ans+=(math.ceil((num-a)/b))+1
    else:
        ans+=1

print(ans)