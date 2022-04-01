N,M=map(int,input().split())

water=[]

for _ in range(N):
    water.append(list(map(int,input().split())))

dr=[0,-1,-1,-1,0,1,1,1]
dc=[-1,-1,0,1,1,1,0,-1]

cloud=[[N-2,0],[N-2,1],[N-1,0],[N-1,1]]
dr2=[1,-1,1,-1]
dc2=[1,1,-1,-1]

for _ in range(M):
    d,s=map(int,input().split())

    for i in range(len(cloud)):
        cloud[i][0]=(cloud[i][0]+(dr[d-1]*s))%N
        cloud[i][1]=(cloud[i][1]+(dc[d-1]*s))%N

    history=set()
    for r,c in cloud:
        water[r][c]+=1
        history.add((r,c))
    cloud=[]

    for r,c in history:
        for j in range(4):
            rr=r+dr2[j]
            cc=c+dc2[j]
            if 0<=rr<N and 0<=cc<N and water[rr][cc]>=1:
                water[r][c]+=1

    for i in range(N):
        for j in range(N):
            if water[i][j]>=2 and (i,j) not in history:
                water[i][j]-=2
                cloud.append([i,j])

ans=0
for i in range(N):
    for j in range(N):
        ans+=water[i][j]

print(ans)