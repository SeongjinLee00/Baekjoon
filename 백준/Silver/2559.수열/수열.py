N,K=map(int,input().split())

numbers=list(map(int,input().split()))

temp=sum(numbers[:K])
ans=sum(numbers[:K])

if K==1:
    print(max(numbers))

else :
    for i in range(1,N-K+1):

        temp=temp-numbers[i-1]+numbers[i+K-1]
        if temp>ans:
            ans=temp

    print(ans)