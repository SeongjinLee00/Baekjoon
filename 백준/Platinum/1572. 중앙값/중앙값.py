import sys
from collections import deque

input = sys.stdin.readline

N,K=map(int,input().split())

size=65536
tree=[0]*(2*size)

def update(n):
    idx=size+n
    while True:
        tree[idx]+=1
        idx//=2
        if idx==0:
            break

def erase(n):
    idx=size+n
    while True:
        tree[idx]-=1
        idx//=2
        if idx==0:
            break

ans=0
def median():
    global ans
    idx=1
    k=(K+1)//2
    while True:
        if tree[2*idx]>=k:
            idx*=2
        else:
            k-=tree[2*idx]
            idx=idx*2+1
        
        if idx>=size:
            ans+=(idx-size)
            break

q=deque()
for _ in range(K):
    n=int(input())
    update(n)
    q.append(n)

for _ in range(N-K):
    median()
    erase(q.popleft())
    n=int(input())
    update(n)
    q.append(n)
median()
print(ans)