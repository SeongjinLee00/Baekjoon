n,m,r=map(int,input().split())

numbers=list(map(int,input().split()))

costs=[[float('inf')]*(n) for _ in range(n)]

for _ in range(r):
    A,B,C=map(int,input().split())

    costs[A-1][B-1]=C
    costs[B-1][A-1]=C

for i in range(n):
    costs[i][i]=0

for k in range(n):
    for i in range(n):
        for j in range(n):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

ans=[]
for row in costs:
    tmp=0
    for i in range(len(row)):
        if row[i]<=m:
            tmp+=numbers[i]
    ans.append(tmp)

print(max(ans))