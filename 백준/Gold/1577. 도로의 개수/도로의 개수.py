N,M=map(int,input().split())

dp=[[0]*(M+1) for _ in range(N+1)]

K=int(input())

constructions=set()
for _ in range(K):
    a,b,c,d=map(int,input().split())

    if (c,d)<(a,b):
        constructions.add((c,d,a,b))
    else:
        constructions.add((a,b,c,d))

for i in range(N+1):
    dp[i][0]=1
    if (i-1,0,i,0) in constructions:
        dp[i][0]-=dp[i-1][0]
        break
for j in range(M+1):
    dp[0][j]=1
    if (0,j-1,0,j) in constructions:
        dp[0][j]-=dp[0][j-1]
        break
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        if (i-1,j,i,j) in constructions:
            dp[i][j]-=dp[i-1][j]
        if (i,j-1,i,j) in constructions:
            dp[i][j]-=dp[i][j-1]

print(dp[N][M])