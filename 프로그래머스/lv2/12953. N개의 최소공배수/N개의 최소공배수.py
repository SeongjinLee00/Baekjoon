from math import gcd

def solution(arr):
    answer = 1
    
    for num in arr:
        g=gcd(answer,num)
        answer=g*(answer//g)*(num//g)
        
    return answer