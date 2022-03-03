import sys
N,M=map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,d=map(int,sys.stdin.readline().split())
    graph[a].append([b,d])
distances=[float('inf')]*(N+1)
distances[1]=0

def BellmanFord():

    for _ in range(N-1): # 일단 N-1번 반복
        for i in range(1,N+1):
            for destination,distance in graph[i]:
                if distances[i]+distance< distances[destination]:
                    distances[destination]=distances[i]+distance

    temp_ans=distances[:]
    for i in range(1,N+1):
        for destination,distance in graph[i]:
            if distances[i]+distance< distances[destination]:
                distances[destination]=distances[i]+distance

    if distances!=temp_ans:
        print(-1)
        exit(0)

BellmanFord()

for i in range(2,len(distances)):
    if distances[i]==float('inf'):
        print(-1)
    else:
        print(distances[i])