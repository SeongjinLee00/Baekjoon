N=int(input())
M=int(input())

costs=[[float('inf')]*(N) for _ in range(N)]

for i in range(N):
    costs[i][i]=0
for _ in range(M):
    A,B,cost=map(int,input().split())

    costs[A-1][B-1]=min(cost,costs[A-1][B-1])

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

for i in range(N):
    for j in range(N):
        if costs[i][j]==float('inf'):
            costs[i][j]=0
    
for i in range(N):
    print(*costs[i])