from collections import deque
import sys
K=int(input())

for _ in range(K):
    V,E=map(int,sys.stdin.readline().split())
    graph=[[] for _ in range(V+1)]

    for _ in range(E):
        a,b=map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited=[0]*(V+1)
    color=[-i for i in range(1,V+2)]
    flag=0

    def bfs(node):
        
        global flag
        q=deque([[node,0]])
        visited[node]=1
        color[node]=0

        while q:
            v,d=q.popleft()
            for w in graph[v]:
                if color[v]==color[w]:
                    print('NO')
                    flag=1
                    return
                if not visited[w]:
                    q.append([w,d+1])
                    visited[w]=1
                    color[w]=(d+1)%2
    
    for i in range(1,V+1):
        if not visited[i] and not flag:
            bfs(i)
    
    if flag==0:
        print('YES')