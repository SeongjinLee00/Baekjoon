def solution(s):
    numbers=list(map(int,s.split()))
    a=max(numbers)
    b=min(numbers)
    
    return f'{b} {a}'