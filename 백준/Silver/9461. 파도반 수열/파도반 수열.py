dp=[0,1,1,1,2,2,3,4,5,7,9]+[0]*91

for i in range(11,101):
    dp[i]=dp[i-1]+dp[i-5]

T=int(input())

for _ in range(T):
    i=int(input())
    print(dp[i])