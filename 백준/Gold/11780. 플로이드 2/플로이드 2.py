from heapq import heappop, heappush
import sys

input= sys.stdin.readline

V=int(input())
E=int(input())

graph=[[] for _ in range(V+1)]

for _ in range(E):
    u,v,w=map(int,input().split())

    graph[u].append([w,v])

def Dijkstra(start):

    distances=[float('inf')]*(V+1)
    path=[[i] for i in range(V+1)]
    distances[start]=0
    q=[]

    heappush(q,[0,start])

    while q:
        travel, curr=heappop(q)

        if distances[curr]<travel:
            continue

        for distance, next in graph[curr]:
            if distances[next]>travel+distance:
                distances[next]=travel+distance
                path[next]=path[curr]+[next]
                heappush(q,[distances[next],next])
    for i in range(len(distances)):
        if distances[i]==float('inf'):
            distances[i]=0
    return distances,path
dd=[]
pp=[]
for i in range(1,V+1):
    d,p=Dijkstra(i)
    dd.append(d)
    pp.append(p)

for row in dd:
    print(*row[1:])

for row in pp:
    for i in range(1,V+1):
        if len(row[i])==1:
            print(0)
            continue
        print(len(row[i]),*row[i])