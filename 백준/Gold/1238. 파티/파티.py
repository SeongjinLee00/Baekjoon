import heapq

N,M,X=map(int,input().split())

graph=[[] for _ in range(N+1)]
graph2=[[] for _ in range(N+1)]
distances=[float('inf')]*(N+1)
distances2=[float('inf')]*(N+1)

for _ in range(M):
    s,e,w=map(int,input().split())
    graph[s].append([w,e])
    graph2[e].append([w,s])

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

def Dijkstra2(start):

    q=[]

    heapq.heappush(q,[0,start])
    distances2[start]=0

    while q:
        curr_travel, curr_location=heapq.heappop(q)

        if curr_travel>distances2[curr_location]:
            continue

        for next_distance, next_destination in graph2[curr_location]:
            distance=curr_travel+next_distance
            if distance<distances2[next_destination]:
                distances2[next_destination]=distance
                heapq.heappush(q,[distance, next_destination])

Dijkstra(X)
Dijkstra2(X)

ans=0
for i in range(1,N+1):
    if distances[i]+distances2[i]>ans:
        ans=distances[i]+distances2[i]

print(ans)