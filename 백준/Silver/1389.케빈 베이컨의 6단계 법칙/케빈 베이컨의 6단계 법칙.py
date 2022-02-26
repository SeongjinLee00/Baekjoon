from collections import deque

N,M=map(int,input().split())

relation=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())

    relation[a].append(b)
    relation[b].append(a)

def bfs(v):
    visited=[v]
    q=deque([[v,0]])
    dsum=0
    while q:
        v,d=q.popleft()
        d+=1
        for w in relation[v]:
            if w not in visited:
                visited.append(w)
                dsum+=d
                q.append([w,d])
    return dsum

data=[]
for i in range(1,N+1):
    data.append([i,bfs(i)])

data.sort(key=lambda data:data[1])

print(data[0][0])