def solution(board, moves):
    N=len(board)
    stack=[]
    ans=0
    for move in moves:
        col=move-1
        
        for i in range(N):
            if board[i][col]:
                if stack and stack[-1]==board[i][col]:
                    ans+=1
                    stack.pop()
                    board[i][col]=0
                    break
                stack.append(board[i][col])
                board[i][col]=0
                break
    print(stack)
    return 2*ans