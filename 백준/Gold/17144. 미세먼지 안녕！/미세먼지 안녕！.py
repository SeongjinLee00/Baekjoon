from pprint import pprint

R,C,T=map(int,input().split())

dust=[]
for _ in range(R):
    dust.append(list(map(int,input().split())))
cleaner=[]
for r in range(R):
    for c in range(C):
        if dust[r][c]==-1:
            cleaner.append([r,c])
top=cleaner[0]
bottom=cleaner[1]

dr=[1,-1,0,0]
dc=[0,0,1,-1]

diffusion=[[0]*C for _ in range(R)]

for _ in range(T):
    for r in range(R):
        for c in range(C):
            diffusion[r][c]=int(dust[r][c]/5)

    for r in range(R):
        for c in range(C):
            cnt=0
            for k in range(4):
                rr=r+dr[k]
                cc=c+dc[k]
                if 0<=rr<R and 0<=cc<C and dust[rr][cc]!=-1:
                    dust[rr][cc]+=diffusion[r][c]
                    cnt+=1
            dust[r][c]-=cnt*diffusion[r][c]

    for r in range(top[0]-1,0,-1):
        dust[r][0]=dust[r-1][0]
    for c in range(0,C-1):
        dust[0][c]=dust[0][c+1]
    for r in range(0,top[0]):
        dust[r][C-1]=dust[r+1][C-1]
    for c in range(C-1,1,-1):
        dust[top[0]][c]=dust[top[0]][c-1]
    dust[top[0]][top[1]+1]=0

    for r in range(bottom[0]+1,R-1):
        dust[r][0]=dust[r+1][0]
    for c in range(0,C-1):
        dust[R-1][c]=dust[R-1][c+1]
    for r in range(R-1,bottom[0],-1):
        dust[r][C-1]=dust[r-1][C-1]
    for c in range(C-1,1,-1):
        dust[bottom[0]][c]=dust[bottom[0]][c-1]

    dust[bottom[0]][bottom[1]+1]=0

print(sum(sum(dust,[]))+2)