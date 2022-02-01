board=[]
numbers=[]
count=0

for _ in range(5):
    board.append(list(map(int,input().split())))

for _ in range(5):
    numbers.append(list(map(int,input().split())))

def call(num):
    for i in range(5):
        for j in range(5):
            if board[i][j]==num:
                board[i][j]=0
def check(lst):
    bingo=0
    if board[0][0]==board[0][1]==board[0][2]==board[0][3]==board[0][4]==0:
        bingo +=1
    if board[1][0]==board[1][1]==board[1][2]==board[1][3]==board[1][4]==0:
        bingo +=1
    if board[2][0]==board[2][1]==board[2][2]==board[2][3]==board[2][4]==0:
        bingo +=1
    if board[3][0]==board[3][1]==board[3][2]==board[3][3]==board[3][4]==0:
        bingo +=1
    if board[4][0]==board[4][1]==board[4][2]==board[4][3]==board[4][4]==0:
        bingo +=1
    if board[0][0]==board[1][0]==board[2][0]==board[3][0]==board[4][0]==0:
        bingo +=1
    if board[0][1]==board[1][1]==board[2][1]==board[3][1]==board[4][1]==0:
        bingo +=1
    if board[0][2]==board[1][2]==board[2][2]==board[3][2]==board[4][2]==0:
        bingo +=1
    if board[0][3]==board[1][3]==board[2][3]==board[3][3]==board[4][3]==0:
        bingo +=1
    if board[0][4]==board[1][4]==board[2][4]==board[3][4]==board[4][4]==0:
        bingo +=1
    if board[0][0]==board[1][1]==board[2][2]==board[3][3]==board[4][4]==0:
        bingo +=1
    if board[4][0]==board[3][1]==board[2][2]==board[1][3]==board[0][4]==0:
        bingo +=1
    return bingo

for i in range(5):
    for j in range(5):
        call(numbers[i][j])
        count += 1

        if check(board)>=3:
            break
    if check(board)>=3:
        break

print(count)