from collections import deque

N=int(input())

q=deque([n for n in range(1,N+1)])

if N==1:
    print(1)
else:
    while True:
        q.popleft()
        q.append(q.popleft())
        if len(q)==1:
            break

    print(q[0])