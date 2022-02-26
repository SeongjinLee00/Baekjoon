from collections import deque

while True:
    w,h=map(int,input().split())
    area=[]
    for _ in range(h):
        area.append(list(map(int,input().split())))

    if w==0 and h==0:
        exit(0)
    cnt=0
    dr=[1,-1,0,0,1,1,-1,-1]
    dc=[0,0,1,-1,1,-1,1,-1]
    def bfs(r,c):
        global cnt
        q=deque([[r,c]])
        area[r][c]=0
        cnt+=1
        while q:
            r,c=q.popleft()
            for i in range(8):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<h and 0<=cc<w and area[rr][cc]==1:
                    q.append([rr,cc])
                    area[rr][cc]=0
    for i in range(h):
        for j in range(w):
            if area[i][j]==1:
                bfs(i,j)

    print(cnt)