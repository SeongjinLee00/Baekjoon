N=int(input())

W=[]

for _ in range(N):
    W.append(list(map(int,input().split())))

ans=99999999999999
def backtrack(cnt, visited, last, s):
    global ans

    if s>ans:
        return

    if cnt==N-1:
        if W[last][0]==0:
            return
        s+=W[last][0]
        if s<ans:
            ans=s
        return

    for i in range(1,N):
        if W[last][i]==0:
            continue
        if not (visited & (1<<i)):
            visited+=(1<<i)
            backtrack(cnt+1,visited,i, s+W[last][i])
            visited-=(1<<i)

backtrack(0,0,0,0)
print(ans)