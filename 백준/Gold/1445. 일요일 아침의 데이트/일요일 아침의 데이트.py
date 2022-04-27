import heapq

N,M=map(int,input().split())

forest=[]
for _ in range(N):
    forest.append(list(input()))

costs=[[1]*(M) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if forest[i][j]=='g':
            if 0<=i+1<N:
                costs[i+1][j]=10000
            if 0<=i-1<N:
                costs[i-1][j]=10000
            if 0<=j+1<M:
                costs[i][j+1]=10000
            if 0<=j-1<M:
                costs[i][j-1]=10000

for i in range(N):
    for j in range(M):
        if forest[i][j]=='g':
            costs[i][j]=100000000
        if forest[i][j]=='S' or forest[i][j]=='F':
            costs[i][j]=1

V=N*M
graph=[[]*(V+1) for _ in range(V+1)]
distances=[float('inf')]*(V+1)

start=0
finish=0
for i in range(N):
    for j in range(M):
        node=i*M+j+1
        if forest[i][j]=='S':
            start=node
        if forest[i][j]=='F':
            finish=node

        if 0<=i+1<N:
            graph[node].append([costs[i+1][j],node+M])
        if 0<=i-1<N:
            graph[node].append([costs[i-1][j],node-M])
        if 0<=j+1<M:
            graph[node].append([costs[i][j+1],node+1])
        if 0<=j-1<M:
            graph[node].append([costs[i][j-1],node-1])

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

Dijkstra(start)
print(distances[finish]//100000000, (distances[finish]-(100000000*(distances[finish]//100000000)))//10000)