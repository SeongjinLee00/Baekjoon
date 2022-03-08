N,M=map(int,input().split())

numbers=[i for i in range(1,N+1)]

def sequence(arr):

    if len(arr)==M:
        print(*arr)
        return

    for n in numbers:
        arr.append(n)
        sequence(arr)
        arr.pop()

sequence([])