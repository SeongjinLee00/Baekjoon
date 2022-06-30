from heapq import heappop, heappush
import sys

input = sys.stdin.readline

maxheap=[] # 음수
minheap=[] # 양수

N=int(input())

for _ in range(N):
    n=int(input())
    if n==0:
        if not maxheap and not minheap:
            print(0)
        elif not maxheap:
            print(heappop(minheap))
        elif not minheap:
            print(-heappop(maxheap))
        else:
            if maxheap[0]<=minheap[0]:
                print(-heappop(maxheap))
            elif maxheap[0]>minheap[0]:
                print(heappop(minheap))
    
    else:
        if n>0:
            heappush(minheap,n)
        else:
            heappush(maxheap,-n)