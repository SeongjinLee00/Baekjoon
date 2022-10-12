T=int(input())

for _ in range(T):
    N=int(input())

    dp=[[0]*N for _ in range(2)]

    stickers=[]

    for _ in range(2):
        stickers.append(list(map(int,input().split())))

    if N==1:
        print(max(stickers[0][0], stickers[1][0]))

    else:
        dp[0][0]=stickers[0][0]
        dp[1][0]=stickers[1][0]

        dp[0][1]=dp[1][0]+stickers[0][1]
        dp[1][1]=dp[0][0]+stickers[1][1]

        for i in range(2,N):
            dp[0][i]=max(dp[1][i-1],dp[0][i-2],dp[1][i-2])+stickers[0][i]
            dp[1][i]=max(dp[0][i-1],dp[0][i-2],dp[1][i-2])+stickers[1][i]
        
        print(max(dp[0][N-1],dp[1][N-1]))