def solution(n):
    answer = 1
    if n==1:
        return 1
    elif n==2:
        return 2
    for i in range(1,n+1):
        answer*=i
    
        if answer>n:
            return i-1