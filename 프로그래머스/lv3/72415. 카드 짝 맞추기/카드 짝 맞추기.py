from collections import deque
from itertools import permutations, product

dr=[1,-1,0,0]
dc=[0,0,1,-1]

def solution(board, r, c):
    answer=9999999
    cards=[[] for _ in range(7)]
    candidate=[]
    memory=[[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            memory[i][j]=board[i][j]
    for i in range(4):
        for j in range(4):
            if board[i][j]!=0:
                cards[board[i][j]].append([i,j])
                if board[i][j] not in candidate:
                    candidate.append(board[i][j])

    candidate.sort()
    repeat=len(candidate)

    def get_min_move(start,end):
        r=start[0]
        c=start[1]

        visited=[[0]*4 for _ in range(4)]

        q=deque([[r,c,0]])
        visited[r][c]=1

        while q:
            r,c,d=q.popleft()
            if [r,c]==end:
                return d
            for i in range(4):
                rr=r+dr[i]
                cc=c+dc[i]
                if 0<=rr<4 and 0<=cc<4 and not visited[rr][cc]:
                    q.append([rr,cc,d+1])
                    visited[rr][cc]=1
            if r==0 and not board[r+1][c] and board[r+2][c] and not visited[r+2][c]:
                q.append([r+2,c,d+1])
                visited[r+2][c]=1
            if r==0 and not board[r+1][c] and not board[r+2][c] and not visited[r+3][c]:
                q.append([r+3,c,d+1])
                visited[r+3][c]=1
            if r==1 and not board[r+1][c] and not visited[r+2][c]:
                q.append([r+2,c,d+1])
                visited[r+2][c]=1

            if c==0 and not board[r][c+1] and board[r][c+2] and not visited[r][c+2]:
                q.append([r,c+2,d+1])
                visited[r][c+2]=1
            if c==0 and not board[r][c+1] and not board[r][c+2] and not visited[r][c+3]:
                q.append([r,c+3,d+1])
                visited[r][c+3]=1
            if c==1 and not board[r][c+1] and not visited[r][c+2]:
                q.append([r,c+2,d+1])
                visited[r][c+2]=1

            if r==3 and not board[r-1][c] and board[r-2][c] and not visited[r-2][c]:
                q.append([r-2,c,d+1])
                visited[r-2][c]=1
            if r==3 and not board[r-1][c] and not board[r-2][c] and not visited[r-3][c]:
                q.append([r-3,c,d+1])
                visited[r-3][c]=1
            if r==2 and not board[r-1][c] and not visited[r-2][c]:
                q.append([r-2,c,d+1])
                visited[r-2][c]=1

            if c==3 and not board[r][c-1] and board[r][c-2] and not visited[r][c-2]:
                q.append([r,c-2,d+1])
                visited[r][c-2]=1
            if c==3 and not board[r][c-1] and not board[r][c-2] and not visited[r][c-3]:
                q.append([r,c-3,d+1])
                visited[r][c-3]=1
            if c==2 and not board[r][c-1] and not visited[r][c-2]:
                q.append([r,c-2,d+1])
                visited[r][c-2]=1

    for order in permutations(candidate,repeat):
        visitlist=[]
        for o in order:
            visitlist.extend(cards[o])
        for p in product([0,1],repeat=repeat):
            visitlist2=[[r,c]]+[[] for _ in range(2*repeat)]
            tmp=0
            for i in range(repeat):
                if p[i]:
                    visitlist2[2*i+1],visitlist2[2*i+2]=visitlist[2*i+1],visitlist[2*i]
                else:
                    visitlist2[2*i+1],visitlist2[2*i+2]=visitlist[2*i],visitlist[2*i+1]
            for j in range(2*repeat):
                tmp+=get_min_move(visitlist2[j],visitlist2[j+1])
                board[visitlist2[j+1][0]][visitlist2[j+1][1]]=0

            if tmp<answer:
                answer=tmp

            for i in range(4):
                for j in range(4):
                    board[i][j]=memory[i][j]

    return answer+repeat*2