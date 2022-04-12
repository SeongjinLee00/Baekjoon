N,K=map(int,input().split())
num=N

a=0
while True:

    num=N+a
    d=num//2
    while True:
        if num<=K:
            print(a)
            exit(0)
        if d==0:
            break
        num-=d
        d=d//2

    a+=1