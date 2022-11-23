def solution(sides):
    answer = 0
    
    for num in range(1,2001):
        tmp=sorted(sides+[num])
        
        if tmp[2]<tmp[1]+tmp[0]:
            answer+=1
    
    return answer