from heapq import heappop, heappush
from itertools import permutations
from collections import defaultdict

import sys

input=sys.stdin.readline

N,M,K=map(int,input().split())

markets=[]

for _ in range(K):
    markets.append(int(input())-1)

graph=[[] for _ in range(N)]

for _ in range(M):
    s,e,c=map(int,input().split())
    graph[s-1].append([c,e-1])
    graph[e-1].append([c,s-1])

def Dijkstra(start):

    distances=[float('inf')]*N
    distances[start]=0
    q=[[0,start]]

    while q:
        curr_distance, curr_destination=heappop(q)

        if distances[curr_destination]<curr_distance:
            continue

        for next_distance, next_destination in graph[curr_destination]:
            distance=curr_distance+next_distance
            if distance<distances[next_destination]:
                heappush(q,[distance,next_destination])
                distances[next_destination]=distance

    return distances

markets_set=set(markets)
memo=defaultdict(list)

markets.sort()
ans=999999999999999999
for i in range(N):
    if i in markets_set:
        memo[i]=Dijkstra(i)

for n in range(N):
    if n in markets_set:
        continue
    for item in permutations(markets,K):
        tmp=0
        for i in range(K-1):
            tmp+=memo[item[i]][item[i+1]]

        tmp+=memo[item[0]][n]
        tmp+=memo[item[-1]][n]

        if tmp<ans:
            ans=tmp

print(ans)