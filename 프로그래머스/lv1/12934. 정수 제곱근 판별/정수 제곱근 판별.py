def solution(n):
    for i in range(1,10**8):
        if i*i==n:
            return i*i+2*i+1
    return -1