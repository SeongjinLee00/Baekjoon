def solution(land):
    dp=[[0]*4 for _ in range(len(land))]
    
    dp[0]=land[0][:]
    
    for i in range(1,len(land)):
        for j in range(4):
            if j==0:
                dp[i][0]=max(dp[i-1][1],dp[i-1][2],dp[i-1][3])+land[i][0]
            elif j==1:
                dp[i][1]=max(dp[i-1][0],dp[i-1][2],dp[i-1][3])+land[i][1]
            elif j==2:
                dp[i][2]=max(dp[i-1][0],dp[i-1][1],dp[i-1][3])+land[i][2]
            elif j==3:
                dp[i][3]=max(dp[i-1][0],dp[i-1][2],dp[i-1][1])+land[i][3]
    
    return max(dp[len(land)-1])