def solution(n):
    ret=[]
    for i in range(1,n+1):
        if not n%i:
            ret.append(i)
    
    return ret