grid=[[0]*1001 for _ in range(1001)]

N=int(input())

for k in range(1,N+1):
    x1,y1,x2,y2=map(int,input().split())

    for i in range(x1,x1+x2):
        for j in range(y1,y1+y2):
            grid[i][j]=k

for k in range(1,N+1):
    count=0
    for i in range(1001):
        for j in range(1001):
            if grid[i][j]==k:
                count +=1
    print(count)