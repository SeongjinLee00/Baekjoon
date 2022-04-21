N=int(input())

dp=[[[0]*10 for _ in range(101)] for _ in range(1024)]
#마지막 숫자, 길이, 현재까지 사용된 숫자(비트마스킹)
for i in range(1, 10):
    dp[1<<i][0][i] = 1

for i in range(1, N):
    for e in range(10):
        for bm in range(1024):
            if e < 9:
                dp[bm|(1<<e)][i][e]+=dp[bm][i-1][e+1]
            if e > 0:
                dp[bm|(1<<e)][i][e]+=dp[bm][i-1][e-1]

print(sum(dp[1023][N-1])%1000000000)