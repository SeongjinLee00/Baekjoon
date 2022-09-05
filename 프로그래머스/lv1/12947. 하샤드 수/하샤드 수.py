def solution(x):
    tmp=0
    num=x
    while num>=1:
        tmp+=num%10
        num//=10

    return not x%tmp