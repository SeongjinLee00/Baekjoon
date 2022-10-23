primes=[1]*1000001

primes[0]=0
primes[1]=0

for num in range(2,1002):
    if primes[num]:
        for i in range(2*num,1000001,num):
            primes[i]=0

N=int(input())

for i in range(2,N+1):
    if primes[i]:
        visited=set()
        memory=i
        while True:
            tmp=0
            for n in str(i):
                tmp+=int(n)**2
            if tmp in visited:
                break
            elif tmp==1:
                print(memory)
                break
            visited.add(tmp)
            i=tmp