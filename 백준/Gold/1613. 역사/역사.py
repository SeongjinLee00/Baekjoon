n,k=map(int,input().split())

costs=[[float('inf')]*n for _ in range(n)]

for _ in range(k):
    a,b=map(int,input().split())

    costs[a-1][b-1]=1

for k in range(n):
    for i in range(n):
        for j in range(n):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

for i in range(n):
    costs[i][i]=0

S=int(input())

for _ in range(S):
    s,e=map(int,input().split())

    if costs[s-1][e-1]==float('inf') and costs[e-1][s-1]==float('inf'):
        print(0)
    elif costs[s-1][e-1]==float('inf') and costs[e-1][s-1]<float('inf'):
        print(1)
    elif costs[s-1][e-1]<float('inf') and costs[e-1][s-1]==float('inf'):
        print(-1)