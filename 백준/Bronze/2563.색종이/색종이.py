grid=[[False]*100 for _ in range(100)]

N=int(input())

for _ in range(N):
    x,y=map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            grid[i][j]=True

count=0
for i in range(100):
    for j in range(100):
        if grid[i][j]==True:
            count +=1

print(count)