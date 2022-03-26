N=int(input())

costs=[[float('inf')]*(N) for _ in range(N)]

while True:
    A,B=map(int,input().split())
    if A==-1 and B==-1:
        break
    costs[A-1][B-1]=1
    costs[B-1][A-1]=1

for i in range(N):
    costs[i][i]=0

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

minscore=999
candidate=[]
for i in range(N):
    row=costs[i]
    if max(row)<minscore:
        candidate=[]
        minscore=max(row)
        candidate.append(i+1)
    elif max(row)==minscore:
        candidate.append(i+1)

print(minscore, len(candidate))
print(*candidate)