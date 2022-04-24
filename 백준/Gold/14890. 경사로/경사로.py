N,L=map(int,input().split())

board=[]

for _ in range(N):
    board.append(list(map(int,input().split())))

board_=list(zip(*board))
def check(road):
    slope=[False]*N

    for i in range(N-1):
        if abs(road[i]-road[i+1])>=2: # 2이상 높이차이나면
            return False

        if road[i+1]==road[i]+1: # 앞으로 한칸 증가하면
            height=road[i]
            for k in range(L): # 뒤에 L칸 봐야함
                if i-k<0:
                    return False
                if road[i-k]!=height:
                    return False
                else:
                    if slope[i-k]==True:
                        return False
                    slope[i-k]=True
        
        if road[i+1]==road[i]-1:
            height=road[i+1]
            for k in range(L):
                if i+1+k>=N:
                    return False
                if road[i+1+k]!=height:
                    return False
                else:
                    if slope[i+1+k]==True:
                        return False
                    slope[i+1+k]=True

    return True
ans=0
for i in range(N):
    ans+=check(board[i])
    ans+=check(board_[i])

print(ans)