def solution(n):
    tmp=0
    for i in range(1,n+1):
        if not n%i:
            tmp+=i
    
    return tmp