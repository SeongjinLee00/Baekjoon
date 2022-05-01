from heapq import heappop, heappush

N,M,T,D=map(int,input().split())

field=[]

for _ in range(N):
    field.append(list(map(ord,(list(input())))))

for i in range(N):
    for j in range(M):
        if 90>=field[i][j]>=65:
            field[i][j]-=65
        if field[i][j]>=97:
            field[i][j]-=71

V=N*M
graph=[[] for _ in range(V)]

for i in range(N):
    for j in range(M):
        node=i*M+j
        if 0<=i+1<N and -T<=field[i+1][j]-field[i][j]<=T:
            if field[i+1][j]-field[i][j]<=0:
                graph[node].append([1,node+M])
            else:
                graph[node].append([(field[i+1][j]-field[i][j])**2,node+M])

        if 0<=i-1<N and -T<=field[i-1][j]-field[i][j]<=T:
            if field[i-1][j]-field[i][j]<=0:
                graph[node].append([1,node-M])
            else:
                graph[node].append([(field[i-1][j]-field[i][j])**2,node-M])

        if 0<=j+1<M and -T<=field[i][j+1]-field[i][j]<=T:
            if field[i][j+1]-field[i][j]<=0:
                graph[node].append([1,node+1])
            else:
                graph[node].append([(field[i][j+1]-field[i][j])**2,node+1])

        if 0<=j-1<M and -T<=field[i][j-1]-field[i][j]<=T:
            if field[i][j-1]-field[i][j]<=0:
                graph[node].append([1,node-1])
            else:
                graph[node].append([(field[i][j-1]-field[i][j])**2,node-1])

def Dijkstra(start,end):
    q=[]
    distances=[float('inf')]*(V)
    heappush(q,[0,start])
    distances[start]=0

    while q:
        travel, curr=heappop(q)

        if distances[curr]<travel:
            continue

        for distance, next in graph[curr]:
            if travel+distance<distances[next]:
                heappush(q,[travel+distance,next])
                distances[next]=travel+distance

    return distances[end]

possible=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if Dijkstra(0,i*M+j)+Dijkstra(i*M+j,0)<=D:
            possible[i][j]=1

ans=0

for i in range(N):
    for j in range(M):
        if possible[i][j] and field[i][j]>ans:
            ans=field[i][j]

print(ans)