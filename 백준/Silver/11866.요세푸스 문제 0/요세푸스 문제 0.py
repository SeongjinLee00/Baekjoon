from collections import deque

N,K=map(int,input().split())

q=deque([n for n in range(1,N+1)])

a=[]
while True:
    for _ in range(K-1):
        q.append(q.popleft())
    a.append(q.popleft())
    if len(q)==0:
        break

print ('<'+', '.join(map(str,a))+'>')