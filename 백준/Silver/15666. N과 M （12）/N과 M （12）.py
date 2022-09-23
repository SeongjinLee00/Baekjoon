N,M=map(int,input().split())
numbers=list(map(int,input().split()))
numbers.sort()

s=set()

def backtrack(arr,m,last):
    if m==M:
        if tuple(arr) in s:
            return
        else:
            print(*arr)
            s.add(tuple(arr))
            return

    for i in range(N):
        if i<last:
            continue
        backtrack(arr+[numbers[i]],m+1,i)

backtrack([],0,-1)