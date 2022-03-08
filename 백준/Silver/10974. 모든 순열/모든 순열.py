N=int(input())
numbers=[i for i in range(1,N+1)]

def backtrack(arr):

    if len(arr)==N:
        print(*arr)
        return
    
    for n in numbers:
        if n not in arr:
            arr.append(n)
            backtrack(arr)
            arr.pop()

backtrack([])