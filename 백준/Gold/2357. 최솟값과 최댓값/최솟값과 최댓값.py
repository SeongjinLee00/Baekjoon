import sys

input=sys.stdin.readline

N,M=map(int,input().split())

maxtree=[0]*(2*N)
mintree=[0]*(2*N)

for i in range(N):
    n=int(input())
    maxtree[i+N]=n
    mintree[i+N]=n
for i in range(N-1,0,-1):
    maxtree[i]=max(maxtree[2*i],maxtree[2*i+1])
    mintree[i]=min(mintree[2*i],mintree[2*i+1])

def getmax(s,e):
    result=-1
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            if maxtree[left]>result:
                result=maxtree[left]
            left+=1
        if not right%2:
            if maxtree[right]>result:
                result=maxtree[right]
            right-=1
        left//=2
        right//=2
    print(result)

def getmin(s,e):
    result=9999999999999
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            if mintree[left]<result:
                result=mintree[left]
            left+=1
        if not right%2:
            if mintree[right]<result:
                result=mintree[right]
            right-=1
        left//=2
        right//=2
    print(result,end=' ')

# def update(idx, num):
#     i=idx+N-1
#     tree[i]=num
#     i//=2
#     while i>=1:
#         tree[i]=(tree[i*2]+tree[i*2+1])
#         i//=2

for _ in range(M):
    a,b=map(int,input().split())

    getmin(a,b)
    getmax(a,b)