grid=[]

for i in range(100):
    grid.append([])
    for j in range(100):
        grid[i].append(False)

for _ in range(4):
    x1,y1,x2,y2=map(int,input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            grid[x][y]=True

count=0
for i in range(100):
    for j in range(100):
        if grid[i][j]==False:
            count = count + 1

print(10000-count)