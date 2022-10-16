from collections import deque

T=int(input())

for _ in range(T):
    flag=False
    N=int(input())

    start=tuple(map(int,input().split()))

    nodes=set()

    for _ in range(N):
        nodes.add(tuple(map(int,input().split())))

    end=tuple(map(int,input().split()))

    nodes.add(end)

    visited=set()

    q=deque([start])
    visited.add(start)

    while q:
        r,c=q.popleft()
        if (r,c)==end:
            print('happy')
            flag=True
            break
        for rr,cc in nodes:
            if abs(rr-r)+abs(cc-c)<=1000 and (rr,cc) not in visited:
                visited.add((rr,cc))
                q.append((rr,cc))

    if not flag:
        print('sad')
