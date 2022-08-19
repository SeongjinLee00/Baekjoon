numbers=[]

for _ in range(9):
    numbers.append(list(map(int,input().split())))

zeros=[]

for i in range(9):
    for j in range(9):
        if numbers[i][j]==0:
            zeros.append((i,j))

N=len(zeros)

def check(r,c,num):
    for i in range(9):
        if numbers[r][i]==num or numbers[i][c]==num:
            return False
    
    if 0<=r<3 and 0<=c<3:
        x=0
        y=0
    if 0<=r<3 and 3<=c<6:
        x=0
        y=3
    if 0<=r<3 and 6<=c<9:
        x=0
        y=6
    if 3<=r<6 and 0<=c<3:
        x=3
        y=0
    if 3<=r<6 and 3<=c<6:
        x=3
        y=3
    if 3<=r<6 and 6<=c<9:
        x=3
        y=6
    if 6<=r<9 and 0<=c<3:
        x=6
        y=0
    if 6<=r<9 and 3<=c<6:
        x=6
        y=3
    if 6<=r<9 and 6<=c<9:
        x=6
        y=6
    
    for i in range(x,x+3):
        for j in range(y,y+3):
            if numbers[i][j]==num:
                return False

    return True

def backtrack(now):
    if now==N:
        for row in numbers:
            print(" ".join(map(str,row)))
        exit(0)
    
    r=zeros[now][0]
    c=zeros[now][1]

    for num in range(1,10):
        if check(r,c,num):
            numbers[r][c]=num
            backtrack(now+1)
            numbers[r][c]=0

backtrack(0)