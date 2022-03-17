N,K=map(int,input().split())

items=[[0,0]]

for _ in range(N):
    items.append(list(map(int,input().split())))

dp=[[0]*(N+1) for _ in range(K+1)]

for i in range(1,K+1):
    for j in range(1,N+1):
        if items[j][0]>i: # N번째 물건의 무게
            dp[i][j]=dp[i][j-1]
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-items[j][0]][j-1]+items[j][1])

print(dp[K][N])