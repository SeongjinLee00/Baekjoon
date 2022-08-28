from heapq import heappop, heappush, heapify
from collections import defaultdict

N,M=map(int,input().split())

C=list(map(int,input().split()))

p=int(input())

reduce=defaultdict(dict)
for _ in range(p):
    a,b,k=map(int,input().split())
    C[b-1]+=k
    reduce[a-1][b-1]=k

q1=[]
for i in range(len(C)):
    q1.append([C[i],i])

heapify(q1)

ans=0
killed=set()
while q1:
    difficulty, idx = heappop(q1)
    if difficulty>ans:
        ans=difficulty
    
    if idx in killed:
        continue
    
    for k, v in reduce[idx].items():
        C[k]-=v
        heappush(q1,[C[k],k])
    
    killed.add(idx)
    if len(killed)==M:
        print(ans)
        exit(0)