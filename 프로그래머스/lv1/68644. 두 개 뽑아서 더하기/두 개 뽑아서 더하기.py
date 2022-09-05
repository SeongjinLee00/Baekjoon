def solution(numbers):
    ret=[]
    N=len(numbers)
    for i in range(N-1):
        for j in range(i+1,N):
            ret.append(numbers[i]+numbers[j])
    
    ret=list(set(ret))
    
    return sorted(ret)