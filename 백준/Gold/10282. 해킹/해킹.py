import heapq

T=int(input())
for _ in range(T):
    V,E,C=map(int,input().split())
    graph=[[] for _ in range(V+1)]
    distances=[float('inf')]*(V+1)

    for _ in range(E):
        u,v,w=map(int,input().split())
        graph[v].append([w,u])
    
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

    Dijkstra(C)

    cnt=0
    time=0

    for number in distances:
        if number<float('inf'):
            cnt+=1
            if number>time:
                time=number

    print(cnt,time)