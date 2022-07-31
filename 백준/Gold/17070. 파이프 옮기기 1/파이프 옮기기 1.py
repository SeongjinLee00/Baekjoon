N=int(input())

numbers=[]
for _ in range(N):
    numbers.append(list(map(int,input().split())))

dp1=[[0]*N for _ in range(N)] # 가로
dp2=[[0]*N for _ in range(N)] # 대각선
dp3=[[0]*N for _ in range(N)] # 세로

dp1[0][1]=1

for i in range(N):
    for j in range(N):
        if i==0 and (j==0 or j==1):
            continue
        if 0<=j-1<N and not numbers[i][j]:
            dp1[i][j]=dp1[i][j-1]+dp2[i][j-1]
        if 0<=i-1<N and 0<=j-1<N and (numbers[i][j]+numbers[i-1][j]+numbers[i][j-1]==0):
            dp2[i][j]=dp1[i-1][j-1]+dp2[i-1][j-1]+dp3[i-1][j-1]
        if 0<=i-1<N and not numbers[i][j]:
            dp3[i][j]=dp2[i-1][j]+dp3[i-1][j]

print(dp1[N-1][N-1]+dp2[N-1][N-1]+dp3[N-1][N-1])