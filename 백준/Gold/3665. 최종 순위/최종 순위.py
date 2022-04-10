T=int(input())

for _ in range(T):
    N=int(input())
    numbers=list(map(int,input().split()))
    M=int(input())
    
    indegree=[0]*(N+1)
    for i in range(N):
        indegree[numbers[i]]=i
    
    graph=[[] for _ in range(N+1)]

    for _ in range(M):
        a,b=map(int,input().split())

        if numbers.index(a)>numbers.index(b): # 원래 a가 b보다 뒤에 있었다면
            indegree[a]-=1
            indegree[b]+=1
        else:
            indegree[a]+=1
            indegree[b]-=1
    
    ans=[0]*(N+1)

    flag=0
    for i in range(1,N+1):
        if ans[indegree[i]]:
            print('IMPOSSIBLE')
            flag=1
            break
        ans[indegree[i]]=i

    ans.pop()

    if flag==0:
        print(*ans)