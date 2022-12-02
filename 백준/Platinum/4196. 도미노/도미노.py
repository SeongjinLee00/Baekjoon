import sys
sys.setrecursionlimit(10**5)
input=sys.stdin.readline

T=int(input())

def dfs(u):
    for v in graph[u]:
        if not visited[v]:
            visited[v]=1
            dfs(v)
    stack.append(u)

def rev_dfs(u):
    scc.append(u)
    for v in rev_graph[u]:
        if not rev_visited[v]:
            rev_visited[v]=1
            rev_dfs(v)

for _ in range(T):
    V,E=map(int,input().split())

    graph=[[] for _ in range(V+1)]
    rev_graph=[[] for _ in range(V+1)]

    for _ in range(E):
        s,e=map(int,input().split())
        graph[s].append(e)
        rev_graph[e].append(s)
    
    visited=[0]*(V+1)
    rev_visited=[0]*(V+1)
    scc_map=[0]*(V+1)

    stack=[]

    sccs=[]

    cnt=1
    for start in range(1,V+1):
        if not visited[start]:
            visited[start]=1
            dfs(start)

    while stack:
        now=stack.pop()
        if not rev_visited[now]:
            scc=[]
            rev_visited[now]=1
            rev_dfs(now)
            sccs.append(scc)
            for node in scc:
                scc_map[node]=cnt
            cnt+=1
    scc_graph=[set() for _ in range(max(scc_map)+1)]

    for i in range(1,V+1):
        now=scc_map[i]
        for j in graph[i]:
            next=scc_map[j]
            if now==next:
                continue
            scc_graph[now].add(next)

    indegree=[0]*len(scc_graph)
    for i in range(1,len(scc_graph)):
        for next in scc_graph[i]:
            indegree[next]+=1
    
    print(indegree.count(0)-1)