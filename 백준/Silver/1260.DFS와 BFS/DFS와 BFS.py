from collections import deque

N,M,V=map(int,input().split())

graph=[[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1

def bfs(start):
    visited=[start]
    need_visited=deque()
    need_visited.append(start)

    while need_visited:
        v=need_visited.popleft()
        print(v,end=' ')

        for w in range(N+1):
            if graph[v][w]==1 and (w not in visited):
                visited.append(w)
                need_visited.append(w)

def dfs(start, visited=[]):
    visited.append(start)
    print(start,end=' ')

    for w in range(N+1):
        if graph[start][w]==1 and (w not in visited):
            dfs(w, visited)

# def dfs_stack(start):
#     visited=[start]
#     need_visited=deque()
#     need_visited.append(start)

#     while need_visited:
#         v=need_visited.pop()
#         print(v,end=' ')

#         for w in range(N+1):
#             if graph[v][w]==1 and (w not in visited):
#                 visited.append(w)
#                 need_visited.append(w)

dfs(V)
print()
bfs(V)
# print()
# dfs_stack(V)