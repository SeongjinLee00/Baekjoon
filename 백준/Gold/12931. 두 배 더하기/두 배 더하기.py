N=int(input())

numbers=list(map(int,input().split()))

ans=0

while True:
    if sum(numbers)==0:
        print(ans)
        exit(0)
    for i in range(len(numbers)):
        if numbers[i]%2:
            numbers[i]-=1
            ans+=1
            break
    else:
        for i in range(len(numbers)):
            numbers[i]//=2
        ans+=1