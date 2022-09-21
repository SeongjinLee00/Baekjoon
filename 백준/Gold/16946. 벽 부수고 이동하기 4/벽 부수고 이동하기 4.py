N,M=map(int,input().split())
board=[]

for _ in range(N):
    board.append(list(map(int,list(input()))))

dr=[1,-1,0,0]
dc=[0,0,1,-1]

board2=[[0]*M for _ in range(N)]

def dfs(r,c,cnt):
    q=[[r,c]]
    visited={(r,c)}
    
    ret=0
    while q:
        r,c=q.pop()
        ret+=1
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<N and 0<=cc<M and (rr,cc) not in visited and not board[rr][cc]:
                visited.add((rr,cc))
                q.append([rr,cc])
    
    for rr,cc in visited:
        board2[rr][cc]=(cnt,ret)

cnt=0
for i in range(N):
    for j in range(M):
        if not board2[i][j] and not board[i][j]:
            cnt+=1
            dfs(i,j,cnt)

ret=[[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board2[i][j]:
            ret[i][j]='0'
        else:
            d=dict()
            tmp=0
            for k in range(4):
                ii=i+dr[k]
                jj=j+dc[k]
                if 0<=ii<N and 0<=jj<M:
                    if board2[ii][jj]==0:
                        continue
                    d[board2[ii][jj][0]]=board2[ii][jj][1]
            for k,v in d.items():
                tmp+=v
            ret[i][j]=str((tmp+1)%10)

for row in ret:
    print("".join(row))