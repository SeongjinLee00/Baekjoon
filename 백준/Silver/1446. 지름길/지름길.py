import heapq
N,D=map(int,input().split())

start=0

graph=[[] for _ in range(D+1)]
distances=[float('inf') for _ in range(D+1)]

for _ in range(N):
    a,b,d=map(int,input().split())
    if b<=D:
        graph[a].append([d,b])

for i in range(len(graph)-1):
    graph[i].append([1,i+1])

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

print(distances[-1])