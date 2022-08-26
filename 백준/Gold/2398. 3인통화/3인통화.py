from heapq import heappop, heappush

N,M=map(int,input().split())

graph=[[] for _ in range(N)]

for _ in range(M):
    s,e,c=map(int,input().split())
    graph[s-1].append([c,e-1])
    graph[e-1].append([c,s-1])

d1,d2,d3=map(int,input().split())

def Dijkstra(start):
    distances=[[float('inf'),[]] for _ in range(N)]
    q=[[0,start,[start]]]
    distances[start]=[0,[start]]

    while q:
        travel, now, path=heappop(q)

        if distances[now][0]<travel:
            continue
        
        for cost, next in graph[now]:
            distance=travel+cost
            if distance<distances[next][0]:
                heappush(q,[distance,next,path+[next]])
                distances[next]=[distance,path+[next]]

    return distances

distances1=Dijkstra(d1-1)
distances2=Dijkstra(d2-1)
distances3=Dijkstra(d3-1)

ans1=9999999999999999
ans2=-1
for k in range(N):
    if distances1[k][0]+distances2[k][0]+distances3[k][0]<ans1:
        ans1=distances1[k][0]+distances2[k][0]+distances3[k][0]
        ans2=k
        ans3=distances1[k][1]
        ans4=distances2[k][1]
        ans5=distances3[k][1]

print(ans1, len(ans3)+len(ans4)+len(ans5)-3)
for i in range(len(ans3)-1):
    if len(ans3)==1:
        break
    print(ans3[i]+1, ans3[i+1]+1)
for i in range(len(ans4)-1):
    if len(ans4)==1:
        break
    print(ans4[i]+1, ans4[i+1]+1)
for i in range(len(ans5)-1):
    if len(ans5)==1:
        break
    print(ans5[i]+1, ans5[i+1]+1)
