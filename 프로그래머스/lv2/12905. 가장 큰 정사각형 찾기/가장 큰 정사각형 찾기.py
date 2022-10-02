def solution(board):

    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if not board[i][j]: continue
            board[i][j]=min(board[i-1][j-1],board[i-1][j],board[i][j-1])+1

    ans=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>ans:
                ans=board[i][j]
    
    return ans*ans