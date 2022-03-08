N,M=map(int,input().split())

numbers=list(map(int,input().split()))
numbers.sort()

def backtrack(arr,idx):

    if len(arr)==M:
        print(*arr)
        return
    
    for i in range(idx,N):
        arr.append(numbers[i])
        backtrack(arr,i+1)
        arr.pop()

backtrack([],0)