import sys

input=sys.stdin.readline

N,M=map(int,input().split())

numbers=[]

for _ in range(N):
    numbers.append(list(map(int,input().split())))

for i in range(N):
    for j in range(N-1):
        numbers[i][j+1]+=numbers[i][j]

for j in range(N):
    for i in range(N-1):
        numbers[i+1][j]+=numbers[i][j]

for _ in range(M):
    r1,c1,r2,c2=map(int,input().split())

    ans=0
    ans+=numbers[r2-1][c2-1]
    if c1>=2: ans-=numbers[r2-1][c1-2]
    if r1>=2: ans-=numbers[r1-2][c2-1]
    if r1>=2 and c1>=2: ans+=numbers[r1-2][c1-2]
    print(ans)