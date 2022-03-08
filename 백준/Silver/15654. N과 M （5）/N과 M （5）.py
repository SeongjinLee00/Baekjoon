N,M=map(int,input().split())

numbers=list(map(int,input().split()))
numbers.sort()

def backtrack(arr):

    if len(arr)==M:
        print(*arr)
        return
    
    for n in numbers:
        if n not in arr:
            arr.append(n)
            backtrack(arr)
            arr.pop()

backtrack([])