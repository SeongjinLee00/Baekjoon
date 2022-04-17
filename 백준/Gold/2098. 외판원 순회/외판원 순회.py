N=int(input())

W=[]

for _ in range(N):
    W.append(list(map(int,input().split())))

dp=[[0]*N for _ in range(1<<N)]

def TSP(visited,now):
    visited|=(1<<now)

    if visited==(1<<N)-1:
        if W[now][0]!=0:
            return W[now][0]
        else:
            return float('inf')
    
    ret=dp[visited][now]

    if ret!=0:
        return ret
    else:
        ret=float('inf')
        for i in range(N):
            if i!=now and not visited&(1<<i) and W[now][i]!=0:
                tmp=TSP(visited,i)+W[now][i]
                ret=min(ret,tmp)
                dp[visited][now]=ret

    return ret

print(TSP(0,0))