N=int(input())
wine=[0]

for _ in range(N):
    wine.append(int(input()))

dp=[0]*(N+1)

if N==1:
    print(wine[1])
    exit(0)
elif N==2:
    print(wine[1]+wine[2])
    exit(0)
dp[1]=wine[1]
dp[2]=wine[1]+wine[2]
dp[3]=max(wine[1]+wine[2],wine[1]+wine[3],wine[2]+wine[3])

for i in range(4,N+1):

    dp[i]=max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i])

print(dp[-1])