def solution(arr, divisor):
    ret=[]
    
    for n in arr:
        if not n%divisor:
            ret.append(n)
    
    if not ret:
        return [-1]
    return sorted(ret)