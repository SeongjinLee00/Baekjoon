from collections import deque

def solution(x, y, n):
    visited=[0]*1000001
    
    q=deque([[x,0]])
    visited[x]=1
    
    while q:
        now, d = q.popleft()
        
        if now==y:
            return d
        
        if 1<=now+n<=1000000 and not visited[now+n]:
            q.append([now+n,d+1])
            visited[now+n] = 1
        if 1<=now*2<=1000000 and not visited[now*2]:
            q.append([now*2,d+1])
            visited[now*2] = 1
        if 1<=now*3<=1000000 and not visited[now*3]:
            q.append([now*3,d+1])
            visited[now*3] = 1
    
    return -1