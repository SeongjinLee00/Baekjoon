K=int(input())
numbers=list(map(int,input().split()))

from collections import deque

s=0
e=len(numbers)-1
q=deque([[s,e,1]])

depth=1
while q:
    s,e,d=q.popleft()
    mid=(s+e)//2
    if d>depth:
        print()
        depth+=1
    print(numbers[mid],end=" ")
    if s==e:
        continue

    q.append([s,mid-1,d+1])
    q.append([mid+1,e,d+1])