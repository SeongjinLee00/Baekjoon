from itertools import combinations
from collections import deque

R,C,D=map(int,input().split())

castle=[]
for _ in range(R):
    castle.append(list(map(int,input().split())))
castle_original=[row[:] for row in castle]
Archers_comb=combinations([i for i in range(C)],3)
dr=[0,-1,0]
dc=[-1,0,1]

maxcnt=0
def search(i):
    q=deque([])
    visited=[[0]*C for _ in range(R)]
    q.append([R,comb[i],0])
    while q:
        r,c,d=q.popleft()
        if r!=R and castle[r][c]==1 and d<=D:
            kill.append([r,c])
            break
        for i in range(3):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<R and 0<=cc<C and not visited[rr][cc]:
                q.append([rr,cc,d+1])
                visited[rr][cc]=1

def turn():
    for c in range(C):
        for r in range(R-1,0,-1):
            castle[r][c]=castle[r-1][c]
    for c in range(C):
        castle[0][c]=0

for comb in Archers_comb:
    castle=[row[:] for row in castle_original]
    cnt=0
    while True:
        kill=[]
        search(0)
        search(1)
        search(2)

        for enemy in kill:
            castle[enemy[0]][enemy[1]]=0
        if len(kill)==3:
            if kill[0]==kill[1] and kill[0]==kill[2] and kill[1]==kill[2]:
                cnt+=1
            elif kill[0]==kill[1] or kill[0]==kill[2] or kill[1]==kill[2]:
                cnt+=2
            else:
                cnt+=3
        elif len(kill)==2:
            if kill[0]==kill[1]:
                cnt+=1
            else:
                cnt+=2
        elif len(kill)==1:
            cnt+=1
        else:
            pass
        
        if cnt>maxcnt:
            maxcnt=cnt
        if sum(sum(castle,[]))==0:
            break
        
        turn()

print(maxcnt)