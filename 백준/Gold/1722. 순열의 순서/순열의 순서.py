N=int(input())
temp=list(map(int,input().split()))

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

if temp[0]==1:
    numbers=[i for i in range(1,N+1)]
    ans=[]
    
    while True:
        if len(ans)==N:
            print(*ans)
            exit(0)

        fact=factorial(len(numbers))
        d=fact//(N-len(ans))
        ans.append(numbers[(temp[1]-1)//d])
        numbers.remove(ans[-1])
        temp[1]%=d

if temp[0]==2:
    numbers=[i for i in range(1,N+1)]
    perm=temp[1:]

    ans=0
    while True:
        fact=factorial(len(numbers))
        d=fact//(len(numbers))
        idx=numbers.index(perm[0])
        ans+=(idx)*d
        perm.remove(numbers[idx])
        numbers.remove(numbers[idx])

        if len(numbers)==0:
            print(ans+1)
            exit(0)