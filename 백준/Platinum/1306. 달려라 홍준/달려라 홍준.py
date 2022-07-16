import sys

input=sys.stdin.readline

N,M=map(int,input().split())

tree=[0]*N+list(map(int,input().split()))

for i in range(N-1,0,-1):
    tree[i]=max(tree[i*2],tree[i*2+1])

def getmax(s,e):
    result=-1
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            if tree[left]>result:
                result=tree[left]
            left+=1
        if not right%2:
            if tree[right]>result:
                result=tree[right]
            right-=1
        left//=2
        right//=2
    print(result,end=' ')

# def update(idx, num):
#     i=idx+N-1
#     tree[i]=num
#     i//=2
#     while i>=1:
#         tree[i]=tree[i*2]+tree[i*2+1]
#         i//=2

for x in range(M,N-M+2):
    getmax(x-(M-1),x+(M-1))