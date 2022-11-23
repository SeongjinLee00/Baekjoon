def solution(A, B):
    if A==B:
        return 0
    for _ in range(len(A)):
        A=A[-1]+A[:len(A)-1]
        
        if A==B:
            return _+1
    
    return -1