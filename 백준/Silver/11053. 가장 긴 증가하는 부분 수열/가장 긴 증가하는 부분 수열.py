N=int(input())
A=list(map(int,input().split()))

A=[0]+A
dp=[1]*(N+1)

dp[0]=0

for i in range(1,N+1):
    for j in range(i):
        if dp[j]>=dp[i] and A[j]<A[i]:
            dp[i]=dp[j]+1

print(max(dp))