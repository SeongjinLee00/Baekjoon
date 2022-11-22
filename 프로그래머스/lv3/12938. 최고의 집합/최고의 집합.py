def solution(n, s):
    if s==1 or n>s:
        return [-1]
    
    base=[s//n]*n
    
    s-=sum(base)
    
    if s==0:
        return base
    
    for i in range(len(base)-1,-1,-1):
        base[i]+=1
        s-=1
        
        if s==0:
            return base