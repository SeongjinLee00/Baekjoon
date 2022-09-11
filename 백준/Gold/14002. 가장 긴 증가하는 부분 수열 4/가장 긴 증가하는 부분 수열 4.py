N=int(input())

numbers=list(map(int,input().split()))

dp=[1]*N

sequence=[[numbers[i]] for i in range(N)]

for i in range(N):
    for j in range(i):
        if numbers[i]>numbers[j] and dp[j]>=dp[i]:
            dp[i]=dp[j]+1
            sequence[i]=sequence[j]+[numbers[i]]

ans=0
idx=-1
for i in range(N):
    if dp[i]>ans:
        ans=dp[i]
        idx=i

print(ans)
print(*sequence[idx])