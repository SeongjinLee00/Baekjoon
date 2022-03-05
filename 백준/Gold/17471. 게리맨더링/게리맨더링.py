from collections import deque
from itertools import combinations

N=int(input())
population=list(map(int,input().split()))
graph=[[] for _ in range(N+1)]

for i in range(1,N+1):
    links=list(map(int,input().split()))[1:]
    for j in range(len(links)):
        graph[i].append(links[j])

cities=[i for i in range(1,N+1)]

def bfs(start):
    visited=[0]*(N+1)
    visited[start]=1
    q=deque([start])

    while q:
        v=q.popleft()
        for w in graph[v]:
            if not visited[w] and w not in forbidden:
                q.append(w)
                visited[w]=1
    return visited

min_difference=999999999
flag=0

for i in range(1,N//2+1):
    combination=combinations(cities,i)
    for area1 in combination:
        area2=[]
        for city in range(1,N+1):
            if city not in area1:
                area2.append(city)
        forbidden=[]
        visited1=bfs(area1[0])
        forbidden=area1
        visited2=bfs(area2[0])

        for city1 in area1:
            if visited1[city1]:
                is_area1_possible_1=1
            else:
                is_area1_possible_1=0
                break
        for city2 in area2:
            if visited2[city2]:
                is_area2_possible_1=1
            else:
                is_area2_possible_1=0
                break

        forbidden=[]
        visited3=bfs(area2[0])
        forbidden=area2
        visited4=bfs(area1[0])

        for city1 in area1:
            if visited4[city1]:
                is_area1_possible_2=1
            else:
                is_area1_possible_2=0
                break
        for city2 in area2:
            if visited3[city2]:
                is_area2_possible_2=1
            else:
                is_area2_possible_2=0
                break

        sum1=0
        sum2=0
        if is_area1_possible_1*is_area2_possible_1*is_area1_possible_2*is_area2_possible_2:
            flag=1
            for city1 in area1:
                sum1+=population[city1-1]
            for city2 in area2:
                sum2+=population[city2-1]
        else:
            continue
        difference=abs(sum1-sum2)

        if difference<min_difference:
            min_difference=difference

if flag==0:
    print(-1)
    exit(0)
else:
    print(min_difference)