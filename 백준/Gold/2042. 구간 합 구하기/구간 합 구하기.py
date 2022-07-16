import sys

input=sys.stdin.readline

N,M,K=map(int,input().split())

tree=[0]*(2*N)

for i in range(N):
    tree[i+N]=int(input())

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

for _ in range(M+K):
    a,b,c=map(int,input().split())

    if a==1:
        update(b,c)
    elif a==2:
        partialsum(b,c)