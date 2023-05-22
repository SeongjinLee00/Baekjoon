def solution(s):
    n=len(s)
    
    dp=[[0]*n for _ in range(n)]
    
    for i in range(n):
        dp[i][i]=1
        if 0<=i<n-1 and s[i+1]==s[i]:dp[i][i+1]=2
        if 1<=i<n and s[i-1]==s[i]:dp[i-1][i]=2
        
    for d in range(2,n):
        for v in range(0,n-d):
            if dp[v+1][d+v-1] and s[v]==s[d+v]: dp[v][d+v]=dp[v+1][d+v-1]+2
    
    ans=0
    for i in range(n):
        for j in range(n):
            ans=max(ans,dp[i][j])
    
    return ans