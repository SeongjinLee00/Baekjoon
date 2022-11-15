N,K=map(int,input().split())
numbers=list(map(int,input().split()))
i=0
j=K
ans=99999999

while True:
    if j==len(numbers)+1:
        K+=1
        i=0
        j=K
        if K==N+1:
            break

    tmp=numbers[i:j]

    m=sum(tmp)/K

    v=0

    for k in range(K):
        v+=(tmp[k]-m)**2

    v/=K

    s=v**0.5

    ans=min(ans,s)

    i+=1
    j+=1

print(ans)