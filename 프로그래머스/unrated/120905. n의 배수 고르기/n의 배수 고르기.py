def solution(n, numlist):
    ret=[]
    
    for num in numlist:
        if num%n==0:
            ret.append(num)
            
    return ret