n,k=map(int,input().split())

coins=[]

for _ in range(n):
    coins.append(int(input()))

coins.sort()

dp=[0]*(k+1)
dp[0]=1

for coin in coins:
    for j in range(coins[0],k+1):
        if j-coin>=0: dp[j]+=dp[j-coin]

print(dp[k])