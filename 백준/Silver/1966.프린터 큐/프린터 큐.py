from collections import deque

T=int(input())

for _ in range(T):

    N,idx=map(int,input().split())
    importance=deque(map(int,input().split()))
    order=0
    printed=0
    
    while printed==0:
        if importance[0]==max(importance):
            importance.popleft()
            order+=1
            if idx>=1:
                idx-=1
            elif idx==0:
                print(order)
                printed+=1
        else:
            importance.append(importance.popleft())
            if idx>=1:
                idx-=1
            elif idx==0:
                idx=len(importance)-1