from collections import deque

def solution(maps):
    answer = []
    
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    
    visited=[[0]*len(maps[0]) for _ in range(len(maps))]
    print(visited)
    def bfs(r,c):
        q=deque([[r,c]])
        visited[r][c]=1
        
        s=int(maps[r][c])
        while q:
            r,c=q.popleft()
            for k in range(4):
                rr=r+dr[k]
                cc=c+dc[k]
                if 0<=rr<len(maps) and 0<=cc<len(maps[0]) and not visited[rr][cc] and maps[rr][cc]!='X':
                    q.append([rr,cc])
                    s+=int(maps[rr][cc])
                    visited[rr][cc]=1

        answer.append(s)            
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j]!='X':
                bfs(i,j)
    if not answer:
        return [-1]
    return sorted(answer)