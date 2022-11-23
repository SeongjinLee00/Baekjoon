def solution(array, n):
    array.sort()
    answer = 999999
    ret=0
    for num in array:
        if abs(n-num)<answer:
            answer=abs(n-num)
            ret=num
            
    return ret