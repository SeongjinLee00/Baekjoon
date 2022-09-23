N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()

s=set()
visited=[0]*N
def backtrack(arr,m):
    if m==M:
        if tuple(arr) in s:
            return
        else:
            print(*arr)
            s.add(tuple(arr))
            return

    for i in range(N):
        if visited[i]:
            continue
        visited[i]=1
        backtrack(arr+[numbers[i]],m+1)
        visited[i]=0

backtrack([],0)