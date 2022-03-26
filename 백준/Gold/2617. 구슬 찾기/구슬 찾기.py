N,M=map(int,input().split())

costs=[[float('inf')]*N for _ in range(N)]
for _ in range(M):
    A,B=map(int,input().split())

    costs[A-1][B-1]=1

for i in range(N):
    costs[i][i]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

ans=0
for i in range(N):
    impossible=0
    lighter=0
    heavier=0
    for j in range(N):
        if costs[i][j]==float('inf') and costs[j][i]==float('inf'):
            impossible+=1
        elif costs[i][j]==float('inf') and costs[j][i]<float('inf'):
            lighter+=1
        elif costs[i][j]<float('inf') and costs[j][i]==float('inf'):
            heavier+=1
    if heavier>N//2 or lighter>N//2:
        ans+=1

print(ans)