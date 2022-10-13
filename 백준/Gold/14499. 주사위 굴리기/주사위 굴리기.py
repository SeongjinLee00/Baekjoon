N,M,x,y,k=map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

t=0
f=0
b=0
rear=0
l=0
r=0

commands=list(map(int,input().split()))

for command in commands:
    if command==1:
        if y==M-1:
            continue
        y+=1
        t,r,b,l=l,t,r,b

    elif command==2:
        if y==0:
            continue
        y-=1
        t,r,b,l=r,b,l,t
    
    elif command==3:
        if x==0:
            continue
        x-=1
        t,f,b,rear=f,b,rear,t
    
    elif command==4:
        if x==N-1:
            continue
        x+=1
        t,f,b,rear=rear,t,f,b

    if board[x][y]==0:
        board[x][y]=b
    else:
        b=board[x][y]
        board[x][y]=0
    
    print(t)