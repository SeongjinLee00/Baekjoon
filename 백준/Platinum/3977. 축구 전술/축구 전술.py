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

for t in range(T):
    V,E=map(int,input().split())

    graph=[[] for _ in range(V)]
    rev_graph=[[] for _ in range(V)]

    for _ in range(E):
        s,e=map(int,input().split())
        graph[s].append(e)
        rev_graph[e].append(s)

    visited=[0]*(V)
    rev_visited=[0]*(V)
    scc_map=[0]*(V)

    stack=[]

    sccs=[]

    cnt=0
    for start in range(V):
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
    scc_graph=[set() for _ in range(max(scc_map))]

    for i in range(V):
        now=scc_map[i]
        for j in graph[i]:
            next=scc_map[j]
            if now==next:
                continue
            scc_graph[now].add(next)

    indegree=[0]*cnt

    for i in range(len(scc_graph)):
        for j in scc_graph[i]:
            indegree[j]+=1
        
    if indegree.count(0)>=2:
        print('Confused')
    else:
        ans=indegree.index(0)
        for i,v in enumerate(scc_map):
            if v==ans:
                print(i)
    if t==T-1:
        break
    input()
    print()