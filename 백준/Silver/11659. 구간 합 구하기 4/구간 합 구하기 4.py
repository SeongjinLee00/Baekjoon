N,M=map(int,input().split())
numbers=list(map(int,input().split()))

import sys
input = sys.stdin.readline

dp=[0]*N

for i in range(N):
    dp[i]=dp[i-1]+numbers[i]

dp = dp+[0]+[0]

for _ in range(M):
    s,e =map(int,input().split())

    print(dp[e-1]-dp[s-2])