N,M=map(int,input().split())

numbers=[i for i in range(1,N+1)]

def sequence(arr):

    if len(arr)>M:
        return

    if len(arr)==M:
        print(*arr)
    
    for n in numbers:
        if n not in arr:
            arr.append(n)
            sequence(arr)
            arr.remove(n)

sequence([])