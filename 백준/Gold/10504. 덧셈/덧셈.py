T=int(input())
s=set()
for i in range(31):
    s.add(2**i)

for _ in range(T):
    N=int(input())
    
    if N in s:
        print('IMPOSSIBLE')
    else:
        for n in range(2,50000):
            check=(2*N-n*n+n)%(2*n)

            if not check:
                a=(2*N-n*n+n)//(2*n)
                if a<=0:
                    print('IMPOSSIBLE')
                    break
                print(N,end=' ')
                print('=',end=' ')
                for l in range(n-1):
                    print(a+l,end=' ')
                    print('+',end=' ')
                print(a+n-1)
                break