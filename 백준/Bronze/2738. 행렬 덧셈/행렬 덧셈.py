N,M=map(int,input().split())

a=[]
b=[]
c=[[0]*M for _ in range(N)]

for _ in range(N):
    a.append(list(map(int,input().split())))

for _ in range(N):
    b.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        c[i][j]=a[i][j]+b[i][j]

for row in c:
    print(*row)