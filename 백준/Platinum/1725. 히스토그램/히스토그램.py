import sys

input=sys.stdin.readline
sys.setrecursionlimit(10**5)

N=int(input())

tree=[[] for _ in range(2*N)]

for i in range(N):
    tree[i+N]=[int(input()),i]

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

ans=0
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
    return result[1]+1

def getans(s,e):
    # print(s,e)
    global ans
    if s>e:
        return
    minidx=partial(s,e)

    area=tree[N+minidx-1][0]*(e-s+1)
    # print(area)

    if area>ans:
        ans=area
    if e==s:
        return
    
    getans(s,minidx-1)
    getans(minidx+1,e)

getans(1,N)
print(ans)