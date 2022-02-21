from collections import deque

N=int(input())

houses=[]

for _ in range(N):
    houses.append(list(input()))

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def bfs(r,c):
    q=deque([[r,c]])
    houses[r][c]='X'
    cnt=1
    while q:
        r,c=q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<N and houses[rr][cc]=='1':
                houses[rr][cc]='X'
                cnt+=1
                q.append([rr,cc])
    return cnt

group=0
cnts=[]
for r in range(N):
    for c in range(N):
        if houses[r][c]=='1':
            cnt=bfs(r,c)
            cnts.append(cnt)
            group+=1

cnts.sort()
print(group)
for n in cnts:
    print(n)