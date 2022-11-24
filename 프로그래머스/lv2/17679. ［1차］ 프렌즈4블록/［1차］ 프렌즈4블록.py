          
def solution(m, n, board):
    R=m
    C=n
    board=[list(row) for row in board]
    
    ans=0
    
    def check():
        ret=set()

        for i in range(R-1):
            for j in range(C-1):
                now=board[i][j]
                if not now:
                    continue
                if board[i][j]==board[i+1][j] and board[i][j]==board[i][j+1] and board[i][j]==board[i+1][j+1]:
                    ret.add((i,j))
                    ret.add((i+1,j))
                    ret.add((i,j+1))
                    ret.add((i+1,j+1))

        return ret

    def fall():
        for j in range(C):
            col=[]
            for i in range(R-1,-1,-1):
                if board[i][j]:
                    col.append(board[i][j])
                    board[i][j]=''
            for i in range(R-1,R-1-len(col),-1):
                board[i][j]=col[R-1-i]
    
    while True:
        ret=check()
        
        if not ret:
            return ans
        
        ans+=len(ret)

        for item in ret:
            board[item[0]][item[1]]=''
        
        fall()
        