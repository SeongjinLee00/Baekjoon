def solution(n):
    target=bin(n)[2:].count('1')
    
    for next in range(n+1,1000001):
        tmp=bin(next)
        
        if tmp[2:].count('1')==target:
            return next