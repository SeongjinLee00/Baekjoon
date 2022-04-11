import sys
from heapq import heappush,heappop
input=sys.stdin.readline

N=int(input())

indegree=[0]*(2*N+1)
graph=[[] for _ in range(2*N+1)]
dic={}
reverse_dic={}
cnt=1
for _ in range(N):
    a,b=input().split()

    if a not in dic:
        dic[a]=cnt
        reverse_dic[cnt]=a
        cnt+=1
    if b not in dic:
        dic[b]=cnt
        reverse_dic[cnt]=b
        cnt+=1

    indegree[dic[b]]+=1
    graph[dic[a]].append(dic[b])

q=[]

for k in reverse_dic:
    if indegree[k]==0:
        heappush(q,[0,reverse_dic[k]])

result=[]
while q:
    d,now=heappop(q)
    result.append(now)

    for w in graph[dic[now]]:
        indegree[w]-=1
        if indegree[w]==0:
            heappush(q,[d+1,reverse_dic[w]])

if len(result)<len(dic):
    print(-1)
    exit(0)

for r in result:
    print(r)