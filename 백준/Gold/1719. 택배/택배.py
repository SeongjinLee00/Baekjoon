N,M=map(int,input().split())

costs=[[float('inf')]*N for _ in range(N)]
routes=[['-']*N for _ in range(N)]

for _ in range(M):
    s,e,cost=map(int,input().split())

    costs[s-1][e-1]=cost
    costs[e-1][s-1]=cost
    routes[s-1][e-1]=e-1
    routes[e-1][s-1]=s-1

for k in range(N):
    costs[k][k]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if costs[i][k]+costs[k][j]<costs[i][j]:
                costs[i][j]=costs[i][k]+costs[k][j]
                routes[i][j]=routes[i][k]

for i in range(N):
    for j in range(N):
        if type(routes[i][j])==int:
            routes[i][j]+=1

for row in routes:
    print(*row)