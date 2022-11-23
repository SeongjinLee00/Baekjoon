def solution(n):
    s=set()
    
    for i in range(2,n+1):
        while n%i==0:
            n//=i
            s.add(i)
    
    return sorted(list(s))