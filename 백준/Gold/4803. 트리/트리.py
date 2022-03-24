case=1
while True:
    N,M=map(int,input().split())

    if N==0 and M==0:
        exit(0)

    graph=[[] for _ in range(N+1)]
    
    for _ in range(M):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(N+1)

    def dfs(node):
        flag=0
        stack=[node]
        visited[node]=1
        
        while stack:
            v=stack.pop()
            for w in graph[v]:
                if v==w: # 자신으로 돌아오는 사이클 있으면
                    flag=1
                if w!=node and w in stack:
                    flag=1
                if not visited[w]:
                    visited[w]=1
                    stack.append(w)
        
        return flag

    cnt=0
    for n in range(1,N+1):
        if not visited[n]:
            d=dfs(n)
            cnt+=(1-d)

    if cnt==0:
        print(f'Case {case}: No trees.')
    elif cnt==1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {cnt} trees.')
    
    case+=1