V,E=map(int,input().split())

costs=[[float('inf')]*(V) for _ in range(V)]

for _ in range(E):
    A,B,cost=map(int,input().split())
    costs[A-1][B-1]=cost

for k in range(V):
    for i in range(V):
        for j in range(V):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

ans=float('inf')

for i in range(V):
    if costs[i][i]<ans:
        ans=costs[i][i]

if ans==float('inf'):
    print(-1)
else:
    print(ans)