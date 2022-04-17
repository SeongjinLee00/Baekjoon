N=int(input())

W=[]

for _ in range(N):
    W.append(list(map(int,input().split())))

def bit(x): 
    answer=0
    while x:
        answer+=(x&1)
        x>>=1
    return answer

dp=[float('inf')]*(1<<N)

dp[0]=0
for i in range(1<<N):
    k=bit(i)
    for j in range(N):
        if not i&(1<<j):
            dp[i|1<<j]=min(dp[i|1<<j],dp[i]+W[k][j])

print(dp[-1])