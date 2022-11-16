dp=[0,-1,1,-1,2,1,3,2,4,3,2,4]+[0]*100000

for i in range(11,len(dp)):
    dp[i]=min(dp[i-2],dp[i-5])+1

N=int(input())

print(dp[N])