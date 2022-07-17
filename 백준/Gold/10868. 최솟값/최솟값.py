import sys

input=sys.stdin.readline

N,M=map(int,input().split())

mintree=[0]*(2*N)

for i in range(N):
    n=int(input())
    mintree[i+N]=n
for i in range(N-1,0,-1):
    mintree[i]=min(mintree[2*i],mintree[2*i+1])

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
    print(result)

for _ in range(M):
    a,b=map(int,input().split())

    getmin(a,b)