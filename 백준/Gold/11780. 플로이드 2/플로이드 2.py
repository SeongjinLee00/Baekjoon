import sys
input=sys.stdin.readline

N=int(input())
M=int(input())

costs=[[float('inf')]*N for _ in range(N)]

for _ in range(M):
    s,e,cost=map(int,input().split())

    costs[s-1][e-1]=min(costs[s-1][e-1],cost)

routes=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        routes[i][j]=[i+1]

for k in range(N):
    costs[k][k]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if costs[i][k]+costs[k][j]<costs[i][j]:
                costs[i][j]=costs[i][k]+costs[k][j]
                routes[i][j]=routes[i][k]+routes[k][j]

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        routes[i][j]+=[j+1]
        if costs[i][j]==float('inf'):
            costs[i][j]=0

for row in costs:
    print(*row)

for row in routes:
    for o in row:
        if len(o)==1:
            print(0)
            continue
        elif costs[o[0]-1][o[-1]-1]==0:
            print(0)
            continue
        print(len(o),*o)