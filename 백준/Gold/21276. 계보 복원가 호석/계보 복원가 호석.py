from collections import deque

import sys
input=sys.stdin.readline

N=int(input())

names=list(input().split())
names.sort()

d=dict()
rd=dict()

for idx, name in enumerate(names):
    d[idx]=name
    rd[name]=idx

M=int(input())

indegree=[0]*N
graph=[[] for _ in range(N)]

for _ in range(M):
    e,s=input().split()
    indegree[rd[e]]+=1
    graph[rd[s]].append(rd[e])

q=deque()
result=[]
result2=[]

for i in range(N):
    if indegree[i]==0:
        q.append(i)
        result2.append(d[i])

result2.sort()
while q:
    now=q.popleft()
    name=d[now]
    sons=[]
    for i in graph[now]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
            sons.append(d[i])
    sons.sort()
    result.append(name+' '+str(len(sons))+' '+' '.join(sons))

result.sort()
print(len(result2))
print(' '.join(result2))
for item in result:
    print(item)