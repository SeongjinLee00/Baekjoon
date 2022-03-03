import sys
import heapq

V,E=map(int,input().split())

start=int(input())

graph=[[] for _ in range(V+1)]
distances=[float('inf') for _ in range(V+1)]

for _ in range(E):
    a,b,d=map(int,sys.stdin.readline().split())
    graph[a].append([d,b])

def Dijkstra(start):
    distances[start]=0
    q=[]
    heapq.heappush(q, [distances[start],start])

    while q:
        curr_distance, curr_destination=heapq.heappop(q)

        if distances[curr_destination] < curr_distance:
            continue

        for new_distance, new_destination in graph[curr_destination]:
            distance=curr_distance+new_distance
            if distance<distances[new_destination]:
                distances[new_destination]=distance
                heapq.heappush(q,[distance,new_destination])

    return 0

Dijkstra(start)

for i in range(1,V+1):
    if distances[i]==float('inf'):
        print('INF')
    else:
        print(distances[i])