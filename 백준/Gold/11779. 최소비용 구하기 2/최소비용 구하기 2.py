import heapq

V=int(input())
E=int(input())

graph=[[] for _ in range(V+1)]
distances=[float('inf')]*(V+1)
path=[[] for _ in range(V+1)]

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([w,v])

s,e=map(int,input().split())

def Dijkstra(start):

    q=[]

    heapq.heappush(q,[0,start])
    distances[start]=0
    path[start]=[start]

    while q:
        curr_travel, curr_location=heapq.heappop(q)

        if curr_travel>distances[curr_location]:
            continue

        for next_distance, next_destination in graph[curr_location]:
            distance=curr_travel+next_distance
            if distance<distances[next_destination]:
                distances[next_destination]=distance
                path[next_destination]=path[curr_location]+[next_destination]
                heapq.heappush(q,[distance, next_destination])

Dijkstra(s)
print(distances[e])
print(len(path[e]))
print(*path[e])