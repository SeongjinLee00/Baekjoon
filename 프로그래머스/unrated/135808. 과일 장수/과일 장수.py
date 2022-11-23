def solution(k, m, score):
    arr=[0]*k
    
    for num in score:
        arr[num-1]+=1
    
    answer=0
    tmp=0
    
    print(arr[::-1])
    for idx,val in enumerate(arr[::-1]):
        tmp+=val
        
        if tmp>=m:
            answer+=(m*(k-idx))*(tmp//m)
            tmp%=m
    
    return answer