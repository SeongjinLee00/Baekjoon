N=int(input())
stairs=[0]
dp=[0]*(N+1)
for _ in range(N):
    stairs.append(int(input()))

if N==1:
    print(stairs[1])
    exit(0)
elif N==2:
    print(stairs[1]+stairs[2])
    exit(0)
    
dp[1]=stairs[1]
dp[2]=stairs[1]+stairs[2]
dp[3]=max(stairs[1]+stairs[3],stairs[2]+stairs[3])

for i in range(4,N+1):
    dp[i]=max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i]) # i-2를 밟은 경우와 안밟은 경우로 나눌 수 있음

print(dp[N])