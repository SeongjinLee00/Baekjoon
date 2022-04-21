N=int(input())

W=[]

for _ in range(N):
    W.append(list(map(int,input().split())))

dp=[[0]*N for _ in range(1<<N)]

def TSP(visited,now):
    visited|=(1<<now) # now 노드 방문처리

    if visited==(1<<N)-1: # 모든 노드를 방문하였으면
        if W[now][0]!=0:
            return W[now][0] # 0으로 가는 거리 반환
        else:
            return float('inf') # 길 없는경우 예외처리
    
    ret=dp[visited][now]

    if ret!=0:
        return ret
    else:
        ret=float('inf')
        for i in range(N):
            if not visited&(1<<i) and W[now][i]!=0: # 나한테로 오는 길 아니고, 방문한적없고, 길 있으면
                tmp=TSP(visited,i)+W[now][i]
                ret=min(ret,tmp)
                dp[visited][now]=ret

    return ret

print(TSP(0,0)) # 어차피 사이클을 이루므로 WLOG 0에서 시작해도됨