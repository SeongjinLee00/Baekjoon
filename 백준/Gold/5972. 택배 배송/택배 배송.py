import heapq
import sys

V,E=map(int,input().split())

graph=[[]*(V+1) for _ in range(V+1)]
distances=[float('inf')]*(V+1)
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append([w,v])
    graph[v].append([w,u])

def Dijkstra(start):
    distances[start]=0
    q=[]
    heapq.heappush(q,[distances[start],start])

    while q:
        curr_travel, curr_location=heapq.heappop(q)
        
        if distances[curr_location]<curr_travel: # 우선순위 큐를 쓰니까, 앞에 긴 경로 빠지기 전에 뒤에 짧은경로가 힙으로 들어올 수 있음
            continue

        for new_distance, new_destination in graph[curr_location]:

            distance=curr_travel+new_distance
            if distance<distances[new_destination]:
                distances[new_destination]=distance
                heapq.heappush(q,[distance,new_destination])

Dijkstra(1)

print(distances[V])