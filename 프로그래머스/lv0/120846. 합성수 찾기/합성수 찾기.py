def solution(n):
    primes={1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
    
    ans=0
    for i in range(1,n+1):
        if i not in primes:
            ans+=1
    
    return ans