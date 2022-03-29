import heapq
import sys

M,N=map(int,input().split())

costs=[]
for _ in range(N):
    costs.append(list(map(int,list(input()))))

V=N*M
graph=[[]*(V+1) for _ in range(V+1)]
distances=[float('inf')]*(V+1)

for i in range(N):
    for j in range(M):
        node=i*M+j+1

        if 0<=i+1<N:
            graph[node].append([costs[i+1][j],node+M])
        if 0<=i-1<N:
            graph[node].append([costs[i-1][j],node-M])
        if 0<=j+1<M:
            graph[node].append([costs[i][j+1],node+1])
        if 0<=j-1<M:
            graph[node].append([costs[i][j-1],node-1])

def Dijkstra(start):
    distances[start]=costs[0][0]
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