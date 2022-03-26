V,E=map(int,input().split())

costs=[[float('inf')]*(V) for _ in range(V)]

for _ in range(E):
    A,B=map(int,input().split())
    costs[A-1][B-1]=1

for i in range(V):
    costs[i][i]=0

for k in range(V):
    for i in range(V):
        for j in range(V):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

costs_=list(zip(*costs))
cnt=0

for i in range(V):
    for j in range(V):
        costs[i][j]=min(costs[i][j],costs_[i][j])

for row in costs:
    if sum(row)<float('inf'):
        cnt+=1
    else:
        pass

print(cnt)