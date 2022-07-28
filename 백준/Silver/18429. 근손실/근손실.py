from itertools import permutations

N,K=map(int,input().split())

numbers=list(map(int,input().split()))

perms=permutations(numbers,N)

ans=0
for item in perms:
    weight=500
    for number in item:
        weight-=K
        weight+=number
        if weight<500:
            ans-=1
            break

    ans+=1

print(ans)