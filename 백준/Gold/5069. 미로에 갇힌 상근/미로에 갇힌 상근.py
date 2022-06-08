dp=[[[0]*28 for _ in range(28)] for _ in range(15)]

dx=[1,-1,0,0,1,-1]
dy=[0,0,1,-1,1,-1]

dp[0][14][14]=1
for i in range(1,15):
    for j in range(28):
        for k in range(28):
            for l in range(6):
                nx=j+dx[l]
                ny=k+dy[l]
                if 0<=nx<28 and 0<=ny<28:
                    dp[i][j][k]+=dp[i-1][nx][ny]

T=int(input())

for _ in range(T):
    print(dp[int(input())][14][14])