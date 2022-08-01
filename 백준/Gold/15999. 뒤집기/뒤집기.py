def pow(num,K):
    if K==0:
        return 1
    elif K==1:
        return num
    else:
        if K%2:
            return pow(num,K//2)*pow(num,K//2)*num
        else:
            return pow(num,K//2)*pow(num,K//2)

N,M=map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(input()))

cnt=0

dr=[1,-1,0,0]
dc=[0,0,1,-1]
for i in range(N):
    for j in range(M):
        color=board[i][j]
        for k in range(4):
            rr=i+dr[k]
            cc=j+dc[k]
            if 0<=rr<N and 0<=cc<M and color!=board[rr][cc]:
                cnt+=1
                break

print(pow(2,N*M-cnt)%1000000007)