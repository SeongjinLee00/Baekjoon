N=int(input())

idx=1

graph=[[] for _ in range(N)]

for _ in range(N):
    n=int(input())
    graph[idx-1].append(n-1)
    idx+=1
cycled=[0]*N

def dfs(start):
    q=[start]
    arr=[start]
    visited=[0]*N
    visited[start]=1
    while q:
        now=q.pop()
        for next in graph[now]:
            if next==start:
                for num in arr:
                    cycled[num]=1
                return len(arr)
            if not visited[next]:
                q.append(next)
                arr.append(next)
                visited[next]=1

for i in range(N):
    if not cycled[i]: dfs(i)

print(sum(cycled))

for i in range(N):
    if cycled[i]:
        print(i+1)