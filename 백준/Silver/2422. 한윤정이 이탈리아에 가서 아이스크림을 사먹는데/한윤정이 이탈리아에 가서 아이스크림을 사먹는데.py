import sys

N, M=map(int, sys.stdin.readline().split())
icecream=[[1]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int, sys.stdin.readline().split())
    icecream[a][b]=0
    icecream[b][a]=0

ans=0

for i in range(1,N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if icecream[i][j]*icecream[j][k]*icecream[i][k]==1:
                ans +=1

print(ans)