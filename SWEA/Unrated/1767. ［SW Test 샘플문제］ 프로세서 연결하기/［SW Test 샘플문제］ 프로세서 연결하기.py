from itertools import combinations

T=int(input())

# direction 0 1 2 3 하 상 우 좌
def check(r,c,direction):
    while True:
        if direction==0:
            r+=1
        elif direction==1:
            r-=1
        elif direction==2:
            c+=1
        elif direction==3:
            c-=1
        
        if r==-1 or r==N or c==-1 or c==N:
            return True
        if board[r][c]!=0:
            return False
        

def connect(r,c,direction):
    ret=0
    while True:
        if direction==0:
            r+=1
        elif direction==1:
            r-=1
        elif direction==2:
            c+=1
        elif direction==3:
            c-=1
        if r==-1 or r==N or c==-1 or c==N: return ret
        ret+=1
        board[r][c]=2
        

def disconnect(r,c,direction):
    ret=0
    while True:
        if direction==0:
            r += 1
        elif direction==1:
            r -= 1
        elif direction==2:
            c += 1
        elif direction==3:
            c -= 1
        if r==-1 or r==N or c==-1 or c==N: return ret
        ret+=1
        board[r][c]=0
        
def backtrack(num, expenses):
    global ans
    global success
    if num == possibility:
        ans = min(ans, expenses)
        success = True
        return
    r = cores[item[num]][0]
    c = cores[item[num]][1]

    for i in range(4):
        if check(r, c, i):
            expenses += connect(r, c, i)
            backtrack(num + 1, expenses)
            expenses -= disconnect(r, c, i)

for tc in range(T):
    N=int(input())
    board=[]
    for _ in range(N):
        board.append(list(map(int,input().split())))

    cores=dict()

    cnt=1
    for i in range(1,N-1):
        for j in range(1,N-1):
            if board[i][j]:
                cores[cnt]=[i,j]
                cnt+=1

    P=len(cores)

    ans=99999999999
    success=False
    for possibility in range(P,0,-1):
        candidate = combinations(cores,possibility)
        for item in candidate:
            backtrack(0,0)
        if success:
            print(f'#{tc+1} {ans}')
            break