N=int(input())
board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

dr=[1,0]
dc=[0,1]

def dfs(r,c):

    if board[r][c]==-1:
        print('HaruHaru')
        exit(0)
    for i in range(2):
        rr=r+dr[i]*board[r][c]
        cc=c+dc[i]*board[r][c]
        if 0<=rr<N and 0<=cc<N and board[r][c]!=0:
            dfs(rr,cc)


dfs(0,0)
print('Hing')
