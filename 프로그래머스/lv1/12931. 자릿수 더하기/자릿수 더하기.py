def solution(n):
    tmp=0
    while n>=1:
        tmp+=n%10
        n//=10
    return tmp