N=int(input())

holes=[]

for _ in range(N):
    holes.append(list(map(int,input().split())))

holes.sort()

graph=[[] for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if holes[i][1]==holes[j][1]:
            if holes[i][0]<holes[j][0]:
                graph[i].append(j)
            else:
                graph[j].append(i)
            break

ans=0
def backtrack(arr, used, cnt):
    global ans
    if arr and arr[0]>=1:
        return

    if cnt==N:
        ans+=check(arr)
        return

    for i in range(0,N):
        if i not in used:
            for c in range(1,i):
                if c not in used:
                    return
            for j in range(i+1, N):
                if j not in used:
                    arr.append(i)
                    arr.append(j)
                    used.add(i)
                    used.add(j)
                    backtrack(arr, used, cnt+2)
                    arr.pop()
                    arr.pop()
                    used.remove(i)
                    used.remove(j)
def check(arr):
    for i in range(len(arr)):
        visited=[0]*N
        visited[arr[i]]=1
        stack=[arr[i]]

        while stack:
            enter = stack.pop()
            for j in range(len(arr)):
                if arr[j]==enter:
                    if j%2:
                        exit=arr[j-1]
                        visited[exit]+=1
                    else:
                        exit=arr[j+1]
                        visited[exit]+=1
                    break

            for next in graph[exit]:
                if visited[next]==2:
                    return 1
                stack.append(next)
                visited[next]+=1
    
    return 0

backtrack([], set(), 0)

print(ans)