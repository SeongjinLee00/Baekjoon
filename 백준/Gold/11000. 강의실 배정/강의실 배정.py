import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

N=int(input())

q1=[]

for _ in range(N):
    s,e=map(int,input().split())
    q1.append([s,e])

heapify(q1)
q2=[]
ans=0
while q1:
    s,e=heappop(q1)

    if q2 and q2[0]<=s:
        heappop(q2)
        heappush(q2,e)
    else:
        ans+=1
        heappush(q2,e)

print(ans)