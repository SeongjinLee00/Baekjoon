import sys

input=sys.stdin.readline

N=int(input())
numbers=list(map(int,input().split()))

tree=[[] for _ in range(2*N)]

for i in range(N):
    tree[i+N]=[numbers[i],i]

for i in range(N-1,0,-1):
    if tree[i*2][0]<tree[i*2+1][0]:
        tree[i]=[tree[i*2][0],tree[i*2][1]]
    elif tree[i*2][0]==tree[i*2+1][0]:
        if tree[i*2][1]<tree[i*2+1][1]:
            tree[i]=[tree[i*2][0],tree[i*2][1]]
        else:
            tree[i]=[tree[i*2+1][0],tree[i*2+1][1]]
    else:
        tree[i]=[tree[i*2+1][0],tree[i*2+1][1]]

def partial(s,e):
    result=[999999999999999999,9999999999999]
    left=s+N-1
    right=e+N-1
    while left<=right:
        if left%2:
            if tree[left][0]<result[0]:
                result=[tree[left][0],tree[left][1]]
            elif tree[left][0]==result[0]:
                if tree[left][1]<result[1]:
                    result=[tree[left][0],tree[left][1]]
                else:
                    pass
            left+=1
        if not right%2:
            if tree[right][0]<result[0]:
                result=[tree[right][0],tree[right][1]]
            elif tree[right][0]==result[0]:
                if tree[right][1]<result[1]:
                    result=[tree[right][0],tree[right][1]]
                else:
                    pass
            right-=1
        left//=2
        right//=2
    print(result[1]+1)

def update(idx, num):
    i=idx+N-1
    tree[i]=[num,idx-1]
    i//=2
    while i>=1:
        if tree[i*2][0]<tree[i*2+1][0]:
            tree[i]=[tree[i*2][0],tree[i*2][1]]
        elif tree[i*2][0]==tree[i*2+1][0]:
            if tree[i*2][1]<tree[i*2+1][1]:
                tree[i]=[tree[i*2][0],tree[i*2][1]]
            else:
                tree[i]=[tree[i*2+1][0],tree[i*2+1][1]]
        else:
            tree[i]=[tree[i*2+1][0],tree[i*2+1][1]]
        i//=2

Q=int(input())
for _ in range(Q):
    try:
        a,b,c=map(int,input().split())
        update(b,c)
    except:
        partial(1,N)