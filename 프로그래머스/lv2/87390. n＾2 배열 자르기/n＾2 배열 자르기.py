def solution(n, left, right):
    ret=[]
    
    for num in range(left,right+1):
        r=(num//n)
        c=(num%n)
        
        ret.append(max(r,c)+1)
    
    return ret