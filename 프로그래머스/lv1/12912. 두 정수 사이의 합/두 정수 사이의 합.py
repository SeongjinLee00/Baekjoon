def solution(a, b):
    tmp=0
    if a>b:
        a,b=b,a
    for n in range(a,b+1):
        tmp+=n
    return tmp