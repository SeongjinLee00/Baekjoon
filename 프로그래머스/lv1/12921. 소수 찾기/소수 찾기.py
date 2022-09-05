def solution(n):
    primes=[0,0]+[1]*1000000
    
    for i in range(2,1000):
        for j in range(2*i,1000000,i):
            primes[j]=0
    
    return sum(primes[:n+1])