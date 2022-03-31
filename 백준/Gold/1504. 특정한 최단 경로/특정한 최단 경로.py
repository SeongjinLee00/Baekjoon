import heapq

V,E=map(int,input().split())

graph=[[] for _ in range(V+1)]
distances=[float('inf')]*(V+1)

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append([w,v])
    graph[v].append([w,u])

v2,v3=map(int,input().split())

def Dijkstra(start):

    q=[]

    heapq.heappush(q,[0,start])
    distances[start]=0

    while q:
        curr_travel, curr_location=heapq.heappop(q)

        if curr_travel>distances[curr_location]:
            continue

        for next_distance, next_destination in graph[curr_location]:
            distance=curr_travel+next_distance
            if distance<distances[next_destination]:
                distances[next_destination]=distance
                heapq.heappush(q,[distance, next_destination])

distances2=[float('inf')]*(V+1)
def Dijkstra2(start):

    q=[]

    heapq.heappush(q,[0,start])
    distances2[start]=0

    while q:
        curr_travel, curr_location=heapq.heappop(q)

        if curr_travel>distances2[curr_location]:
            continue

        for next_distance, next_destination in graph[curr_location]:
            distance=curr_travel+next_distance
            if distance<distances2[next_destination]:
                distances2[next_destination]=distance
                heapq.heappush(q,[distance, next_destination])

distances3=[float('inf')]*(V+1)
def Dijkstra3(start):

    q=[]

    heapq.heappush(q,[0,start])
    distances3[start]=0

    while q:
        curr_travel, curr_location=heapq.heappop(q)

        if curr_travel>distances3[curr_location]:
            continue

        for next_distance, next_destination in graph[curr_location]:
            distance=curr_travel+next_distance
            if distance<distances3[next_destination]:
                distances3[next_destination]=distance
                heapq.heappush(q,[distance, next_destination])

Dijkstra(1)
Dijkstra2(v2)
Dijkstra3(v3)

d1=distances[v2]+distances2[v3]+distances3[V]
d2=distances[v3]+distances3[v2]+distances2[V]

if d1==float('inf') and d2==float('inf'):
    print(-1)
else:
    print(min(d1,d2))