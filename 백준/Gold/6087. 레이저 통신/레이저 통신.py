from heapq import heappop, heappush

C,R=map(int,input().split())

board=[]

for _ in range(R):
    board.append(list(input()))

start=[]
end=[]
for i in range(R):
    for j in range(C):
        if board[i][j]=='C':
            if start:
                end=[i,j]
            else:
                start=[i,j]

dr=[1,-1,0,0]
dc=[0,0,1,-1]
q=[[0,start[0],start[1],0]]
visited=[[float('inf')]*C for _ in range(R)]

while q:
    distance,r,c,direction=heappop(q)

    if r==end[0] and c==end[1]:
        print(distance//10000)
        break
    for i in range(4):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<R and 0<=cc<C and (board[rr][cc]=='.' or board[rr][cc]=='C'):
            if direction==0:
                heappush(q,[1,rr,cc,i+1])
                visited[rr][cc]=1
            elif direction==i+1 and visited[rr][cc]>=distance+1:
                heappush(q,[distance+1,rr,cc,i+1])
                visited[rr][cc]=distance+1
            elif direction!=i+1 and visited[rr][cc]>=distance+10000:
                heappush(q,[distance+10000,rr,cc,i+1])
                visited[rr][cc]=distance+10000