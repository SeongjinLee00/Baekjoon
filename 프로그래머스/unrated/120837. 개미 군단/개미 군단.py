def solution(hp):
    dp=[0]*(1001)
    
    dp[1]=1
    dp[2]=2
    dp[3]=1
    dp[4]=2
    dp[5]=1
    
    for i in range(6,hp+1):
        dp[i]=min(dp[i-5],dp[i-3],dp[i-1])+1
    
    return dp[hp]