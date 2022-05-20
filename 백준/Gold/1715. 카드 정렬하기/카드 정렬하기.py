from heapq import heappop, heappush, heapify
import sys
input=sys.stdin.readline

N=int(input())

q=[]

for _ in range(N):
    q.append(int(input()))

ans=0

heapify(q)

for _ in range(N-1):
    s=heappop(q)+heappop(q)
    ans+=s
    heappush(q,s)

print(ans)