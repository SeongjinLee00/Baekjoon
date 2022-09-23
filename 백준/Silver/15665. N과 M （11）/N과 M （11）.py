N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()

s=set()

def backtrack(arr,m):
    if m==M:
        if tuple(arr) in s:
            return
        else:
            print(*arr)
            s.add(tuple(arr))
            return

    for i in range(N):
        backtrack(arr+[numbers[i]],m+1)

backtrack([],0)