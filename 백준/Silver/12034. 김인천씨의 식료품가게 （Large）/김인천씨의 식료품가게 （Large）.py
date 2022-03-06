T=int(input())

for t in range(1,T+1):
    N=int(input())
    numbers=list(map(int,input().split()))
    ans=[]
    for _ in range(N):
        price=numbers.pop(0)
        if price*4//3 in numbers:
            ans.append(price)
            numbers.remove(price*4//3)

    print(f'Case #{t}:',end=' ')
    print(*ans)