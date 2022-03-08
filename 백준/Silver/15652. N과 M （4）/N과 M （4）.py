N,M=map(int,input().split())

numbers=[i for i in range(1,N+1)]

def sequence(arr,start):

    if len(arr)==M:
        print(*arr)
        return

    for n in range(start,N+1):
        arr.append(n)
        sequence(arr,n)
        arr.pop()

sequence([],1)