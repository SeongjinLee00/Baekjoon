N=int(input())
k=0

for i in range(1,8):
    if 3**i==N:
        k=i

arr=[[' ']*N for _ in range(N)]

def stars(d,i,j):

    if d==0:
        arr[i][j]='*'
        return
    
    l=3**d
    idx=[i,i+l//3,i+l//3*2]
    jdx=[j,j+l//3,j+l//3*2]
    
    stars(d-1,idx[0],jdx[0])
    stars(d-1,idx[0],jdx[1])
    stars(d-1,idx[0],jdx[2])
    stars(d-1,idx[1],jdx[0])
    # stars(d-1,idx[1],jdx[1])
    stars(d-1,idx[1],jdx[2])
    stars(d-1,idx[2],jdx[0])
    stars(d-1,idx[2],jdx[1])
    stars(d-1,idx[2],jdx[2])

stars(k,0,0)
for row in arr:
    print(''.join(row))