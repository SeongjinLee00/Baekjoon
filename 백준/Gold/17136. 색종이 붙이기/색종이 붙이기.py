N=10

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))
C=0

for i in range(N):
    for j in range(N):
        if numbers[i][j]:
            C+=1

if C==0:
    print(0)
    exit(0)

def check(r, c):
    for size in range(2,6):
        for i in range(r,r+size):
            for j in range(c,c+size):
                if i==N or j==N or numbers[i][j]==0:
                    return size-1
    return 5

def attach(r, c, size):
    for i in range(r,r+size):
        for j in range(c,c+size):
            numbers[i][j]=0

def detach(r, c, size):
    for i in range(r,r+size):
        for j in range(c,c+size):
            numbers[i][j]=1

cnt=0
ans=99999999
remain=[5,5,5,5,5]
def backtrack(r, c, m):
    global cnt
    global ans
    if m>=ans:
        return
    if r>=9 and c>9:
        ans=min(ans,m)
        return
    if c>9:
        backtrack(r+1,0,m)
        return

    if numbers[r][c]:
        for k in range(1,check(r,c)+1):
            if remain[k-1]>0:
                attach(r,c,k)
                cnt+=k*k
                remain[k-1]-=1
                backtrack(r, c+1, m+1)
                detach(r,c,k)
                cnt-=k*k
                remain[k-1]+=1
    else:
        backtrack(r,c+1,m)

backtrack(0, 0, 0)
if ans==99999999:
    print(-1)
    exit(0)
print(ans)