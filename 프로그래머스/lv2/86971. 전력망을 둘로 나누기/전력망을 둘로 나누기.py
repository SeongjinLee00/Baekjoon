from collections import deque

def solution(n, wires):
    graph=[[] for _ in range(n)]
    
    for wire in wires:
        graph[wire[0]-1].append(wire[1]-1)
        graph[wire[1]-1].append(wire[0]-1)
    
    def bfs(now):
        q=deque([now])
        cnt=1
        visited[now]=1
        
        while q:
            n=q.popleft()
            for next in graph[n]:
                if not visited[next]:
                    visited[next]=1
                    q.append(next)
                    cnt+=1
        
        return cnt
    ans=999999999999
    for i in range(len(wires)):
        visited=[0]*n
        graph[wires[i][0]-1].remove(wires[i][1]-1)
        graph[wires[i][1]-1].remove(wires[i][0]-1)
        
        for node in range(n):
            if not visited[node]:
                a1=bfs(node)
            break
        for node2 in range(node+1,n):
            if not visited[node2]:
                a2=bfs(node2)
        ans=min(ans,abs(a1-a2))
        graph[wires[i][0]-1].append(wires[i][1]-1)
        graph[wires[i][1]-1].append(wires[i][0]-1)
    return ans