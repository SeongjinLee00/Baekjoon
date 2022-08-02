import sys

input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

tree=[0]*(2*N)

for i in range(N):
    tree[i+N]=numbers[i]

for i in range(N-1,0,-1):
    tree[i]=min(tree[i*2],tree[i*2+1])

def partial(s,e):
    result=999999999999999999
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            result=min(tree[left],result)
            left+=1
        if not right%2:
            result=min(tree[right],result)
            right-=1
        left//=2
        right//=2
    print(result)

def update(idx, num):
    i=idx+N-1
    tree[i]=num
    i//=2
    while i>=1:
        tree[i]=min(tree[i*2],tree[i*2+1])
        i//=2

Q=int(input())
for _ in range(Q):
    a,b,c=map(int,input().split())

    if a==1:
        update(b,c)
    elif a==2:
        partial(b,c)