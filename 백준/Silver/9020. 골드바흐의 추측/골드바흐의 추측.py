numbers=[True]*10001
numbers[0]=False
numbers[1]=False

primes=set()
for i in range(2,10001):
    if numbers[i]:
        primes.add(i)
        for j in range(2*i,10001,i):
            numbers[j]=False

T=int(input())

for _ in range(T):
    n=int(input())

    hn=n//2

    for k in range(hn):
        if hn-k in primes and hn+k in primes:
            print(hn-k, hn+k)
            break