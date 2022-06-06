def factorial(n):
    tmp=1

    for i in range(1,n+1):
        tmp*=i

    return tmp

def C(n,r):
    return factorial(n)//(factorial(n-r)*factorial(r))

N,M,K=map(int,input().split())

if K==0:
    print(C(N+M-2,N-1))
    exit(0)

c=(K-1)%M+1
r=(K-1)//M+1

print(C(r-1+c-1,r-1)*C(N-r+M-c,N-r))