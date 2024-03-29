import sys

input=sys.stdin.readline

N,Q=map(int,input().split())

numbers=list(map(int,input().split()))
tree=[0]*(N)
tree+=numbers

# for i in range(N):
#     tree[i+N]=int(input())

for i in range(N-1,0,-1):
    tree[i]=tree[i*2]+tree[i*2+1]

def partialsum(s,e):
    result=0
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            result+=tree[left]
            left+=1
        if not right%2:
            result+=tree[right]
            right-=1
        left//=2
        right//=2
    print(result)

def update(idx, num):
    i=idx+N-1
    tree[i]=num
    i//=2
    while i>=1:
        tree[i]=tree[i*2]+tree[i*2+1]
        i//=2

for _ in range(Q):
    a,b,c,d=map(int,input().split())

    if a>b:
        partialsum(b,a)
    else:
        partialsum(a,b)
    
    update(c,d)