from heapq import heappop, heappush
import sys

input = sys.stdin.readline

N=int(input())

q=[]

for _ in range(N):
    n=int(input())

    if n==0:
        if not q:
            print(0)
        else:
            print(-heappop(q))
    else:
        heappush(q,-n)