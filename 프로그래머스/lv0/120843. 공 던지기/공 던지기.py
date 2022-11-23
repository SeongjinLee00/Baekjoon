def solution(numbers, k):
    N=len(numbers)
    now=1
    
    for _ in range(k-1):
        now=(now+2)%N
    
    return now