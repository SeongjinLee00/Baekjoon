T=int(input())

for _ in range(T):

    N,M=map(int,input().split())

    head=1
    foot=1

    for i in range(M,M-N,-1):
        head *= i

    for j in range(1,N+1):
        foot *= j

    print(head//foot)