R,C=map(int,input().split())
board=[]

for _ in range(R):
    board.append(list(map(int,input().split())))

memory = [row[:] for row in board]

cctv=[]

for i in range(R):
    for j in range(C):
        if 1<=board[i][j]<=5:
            cctv.append([board[i][j],i,j])

N=len(cctv)

ans=9999999
def check(arr):
    global ans
    board = [row[:] for row in memory]

    def connect(r,c,direction):
        while True:
            if direction==0:
                r+=1
            elif direction==1:
                c+=1
            elif direction==2:
                r-=1
            elif direction==3:
                c-=1
            if r==-1 or r==R or c==-1 or c==C or board[r][c]==6: return
            board[r][c]=7

    for num in range(N):
        t = cctv[num][0]
        r = cctv[num][1]
        c = cctv[num][2]
        case = arr[num]

        if t==1:
            connect(r,c,case)
        elif t==2:
            connect(r,c,case)
            connect(r,c,case+2)
        elif t==3:
            connect(r,c,case)
            connect(r,c,(case+1)%4)
        elif t==4:
            connect(r,c,case)
            connect(r,c,(case+1)%4)
            connect(r,c,(case+2)%4)
        elif t==5:
            connect(r,c,0)
            connect(r,c,1)
            connect(r,c,2)
            connect(r,c,3)
    cnt=0
    for i in range(R):
        for j in range(C):
            if board[i][j]==0:
                cnt+=1

    ans=min(ans,cnt)

def cases(num,arr):

    if num==N:
        check(arr)
        return

    t=cctv[num][0]

    if t==1 or t==3 or t==4:
        cases(num+1,arr+[0])
        cases(num+1,arr+[1])
        cases(num+1,arr+[2])
        cases(num+1,arr+[3])
    elif t==2:
        cases(num+1,arr+[0])
        cases(num+1,arr+[1])
    elif t==5:
        cases(num+1,arr+[0])

cases(0,[])

print(ans)