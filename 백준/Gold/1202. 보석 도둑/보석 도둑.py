import sys
from heapq import heappop, heappush, heapify
input = sys.stdin.readline

N,K=map(int,input().split())

jewels=[]
bags=[]
for _ in range(N):
    m,v=map(int,input().split())
    jewels.append([m,v])

for _ in range(K):
    c=int(input())
    bags.append(c)

bags.sort()
jewels.sort()

temp=[]
cnt=0
answer=0
for bag in bags:
    while True:
        if cnt==N:
            break
        if jewels[cnt][0]<=bag:
            heappush(temp, -jewels[cnt][1])
            cnt+=1
        else:
            break
    
    if temp:
        answer+=(-heappop(temp))

print(answer)