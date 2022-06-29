R,C=map(int,input().split())

board=[]

for _ in range(R):
    board.append(list(input()))

ans=0
visited=[[0]*C for _ in range(R)]

def dfs(r,c,path):
    global ans
    global flag

    visited[r][c]=1
    
    if c==C-1:
        ans+=1
        flag=1
        return

    if r!=0 and not visited[r-1][c+1] and board[r-1][c+1]=='.' and not flag:
        dfs(r-1,c+1,path+[[r-1,c+1]])

    if not visited[r][c+1] and board[r][c+1]=='.' and not flag:
        dfs(r,c+1,path+[[r,c+1]])

    if r!=R-1 and not visited[r+1][c+1] and board[r+1][c+1]=='.' and not flag:
        dfs(r+1,c+1,path+[[r+1,c+1]])

for r in range(0,R):
    flag=0
    dfs(r,0,[[r,0]])

print(ans)