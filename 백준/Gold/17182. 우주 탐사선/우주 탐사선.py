from itertools import permutations

N,K=map(int,input().split())

costs=[]

for _ in range(N):
    costs.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            costs[i][j]=min(costs[i][j],costs[i][k]+costs[k][j])

candidate=[i for i in range(N)]

candidate.remove(K)

ans=99999999999999999999
for order in permutations(candidate,N-1):
    tmp=0
    tmp+=costs[K][order[0]]
    for i in range(N-2):
        tmp+=costs[order[i]][order[i+1]]
    
    if tmp<ans:
        ans=tmp

print(ans)