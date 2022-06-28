N,K=map(int,input().split())

color=[]

for _ in range(N):
    color.append(list(map(int,input().split())))

board=[[[] for _ in range(N)] for _ in range(N)]

num=1
direction=dict()
location=[0]*(K+1)
for _ in range(K):
    r,c,d=map(int,input().split())

    board[r-1][c-1].append(num)
    direction[num]=d
    location[num]=[r-1,c-1]
    num+=1
    
turn=1

while True:
    for i in range(1,K+1):
        d=direction[i]
        r,c=location[i][0],location[i][1]

        if not board[r][c][0]==i:
            continue

        if d==1:
            if c==N-1:
                direction[i]=2
                if color[r][c-1]==2:
                    continue
                elif color[r][c-1]==0:
                    for j in board[r][c]:
                        location[j][1]-=1
                    board[r][c-1].extend(board[r][c])
                    if len(board[r][c-1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c-1]==1:
                    for j in board[r][c]:
                        location[j][1]-=1
                    board[r][c-1].extend(board[r][c][::-1])
                    if len(board[r][c-1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
            else:
                if color[r][c+1]==2:
                    direction[i]=2
                    if c==0 or color[r][c-1]==2:
                        continue
                    for j in board[r][c]:
                        location[j][1]-=1
                    if color[r][c-1]==0: board[r][c-1].extend(board[r][c])
                    if color[r][c-1]==1: board[r][c-1].extend(board[r][c][::-1])
                    if len(board[r][c-1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c+1]==0:
                    for j in board[r][c]:
                        location[j][1]+=1
                    board[r][c+1].extend(board[r][c])
                    if len(board[r][c+1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c+1]==1:
                    for j in board[r][c]:
                        location[j][1]+=1
                    board[r][c+1].extend(board[r][c][::-1])
                    if len(board[r][c+1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
        elif d==2:
            if c==0:
                direction[i]=1
                if color[r][c+1]==2:
                    continue
                elif color[r][c+1]==0:
                    for j in board[r][c]:
                        location[j][1]+=1
                    board[r][c+1].extend(board[r][c])
                    if len(board[r][c+1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c+1]==1:
                    for j in board[r][c]:
                        location[j][1]+=1
                    board[r][c+1].extend(board[r][c][::-1])
                    if len(board[r][c+1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
            else:
                if color[r][c-1]==2:
                    direction[i]=1
                    if c==N-1 or color[r][c+1]==2:
                        continue
                    for j in board[r][c]:
                        location[j][1]+=1
                    if color[r][c+1]==0:board[r][c+1].extend(board[r][c])
                    if color[r][c+1]==1:board[r][c+1].extend(board[r][c][::-1])
                    if len(board[r][c+1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c-1]==0:
                    for j in board[r][c]:
                        location[j][1]-=1
                    board[r][c-1].extend(board[r][c])
                    if len(board[r][c-1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r][c-1]==1:
                    for j in board[r][c]:
                        location[j][1]-=1
                    board[r][c-1].extend(board[r][c][::-1])
                    if len(board[r][c-1])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
        elif d==3:
            if r==0:
                direction[i]=4
                if color[r+1][c]==2:
                    continue
                elif color[r+1][c]==0:
                    for j in board[r][c]:
                        location[j][0]+=1
                    board[r+1][c].extend(board[r][c])
                    if len(board[r+1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r+1][c]==1:
                    for j in board[r][c]:
                        location[j][0]+=1
                    board[r+1][c].extend(board[r][c][::-1])
                    if len(board[r+1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
            else:
                if color[r-1][c]==2:
                    direction[i]=4
                    if r==N-1 or color[r+1][c]==2:
                        continue
                    for j in board[r][c]:
                        location[j][0]+=1
                    if color[r+1][c]==0:board[r+1][c].extend(board[r][c])
                    if color[r+1][c]==1:board[r+1][c].extend(board[r][c][::-1])
                    if len(board[r+1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r-1][c]==0:
                    for j in board[r][c]:
                        location[j][0]-=1
                    board[r-1][c].extend(board[r][c])
                    if len(board[r-1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r-1][c]==1:
                    for j in board[r][c]:
                        location[j][0]-=1
                    board[r-1][c].extend(board[r][c][::-1])
                    if len(board[r-1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
        elif d==4:
            if r==N-1:
                direction[i]=3
                if color[r-1][c]==2:
                    continue
                elif color[r-1][c]==0:
                    for j in board[r][c]:
                        location[j][0]-=1
                    board[r-1][c].extend(board[r][c])
                    if len(board[r-1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r-1][c]==1:
                    for j in board[r][c]:
                        location[j][0]-=1
                    board[r-1][c].extend(board[r][c][::-1])
                    if len(board[r-1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
            else:
                if color[r+1][c]==2:
                    direction[i]=3
                    if r==0 or color[r-1][c]==2:
                        continue
                    for j in board[r][c]:
                        location[j][0]-=1
                    if color[r-1][c]==0:board[r-1][c].extend(board[r][c])
                    if color[r-1][c]==1:board[r-1][c].extend(board[r][c][::-1])
                    if len(board[r-1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r+1][c]==0:
                    for j in board[r][c]:
                        location[j][0]+=1
                    board[r+1][c].extend(board[r][c])
                    if len(board[r+1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]
                elif color[r+1][c]==1:
                    for j in board[r][c]:
                        location[j][0]+=1
                    board[r+1][c].extend(board[r][c][::-1])
                    if len(board[r+1][c])>=4:
                        print(turn)
                        exit(0)
                    board[r][c]=[]

    turn+=1
    if turn>1000:
        print(-1)
        exit(0)