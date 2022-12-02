import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)

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

V,E=map(int,input().split())


graph=[[] for _ in range(V+1)]
rev_graph=[[] for _ in range(V+1)]
visited=[0]*(V+1)
rev_visited=[0]*(V+1)

for _ in range(E):
    s,e=map(int,input().split())
    graph[s].append(e)
    rev_graph[e].append(s)

stack=[]

for start in range(1,V+1):
    if not visited[start]:
        visited[start]=1
        dfs(start)

ans=[]

while stack:
    now=stack.pop()
    if not rev_visited[now]:
        scc=[]
        rev_visited[now]=1
        rev_dfs(now)
        ans.append(scc)

for i in range(len(ans)):
    ans[i].sort()
ans.sort(key=lambda x:x[0])
print(len(ans))

for item in ans:
    print(*item,end=' ')
    print('-1')