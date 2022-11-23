def solution(board):
    dr=[1,-1,0,0,1,1,-1,-1]
    dc=[0,0,1,-1,1,-1,1,-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==1:
                for k in range(8):
                    if 0<=i+dr[k]<len(board) and 0<=j+dc[k]<len(board[0]) and board[i+dr[k]][j+dc[k]]==0:
                        board[i+dr[k]][j+dc[k]]=2
    
    ans=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==0:
                ans+=1
    print(board)
    return ans