N=int(input())

numbers=list(map(int,input().split()))

dp=[0]*N
dp=numbers[::]
for i in range(N):
    for j in range(i-1,-1,-1):
        if numbers[i]>numbers[j]:
            dp[i]=max(dp[i],dp[j]+numbers[i])

print(max(dp))