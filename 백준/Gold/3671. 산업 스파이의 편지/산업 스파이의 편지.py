from itertools import combinations, permutations

primes=[True]*10000000
primes[0]=False
primes[1]=False

for n in range(2,10000000):
    if primes[n]:
        for i in range(2*n,10000000,n):
            primes[i]=False

T=int(input())
for _ in range(T):
    numbers=input()
    N=len(numbers)
    s=set()
    for k in range(1,8):
        selected=combinations([i for i in range(N)], k)
        for item in selected:
            orders=permutations(item,k)
            for order in orders:
                tmp=''
                for number in order:
                    tmp+=numbers[number]
                s.add(int(tmp))
    
    ans=0
    for candidate in s:
        if primes[candidate]:
            ans+=1
    
    print(ans)