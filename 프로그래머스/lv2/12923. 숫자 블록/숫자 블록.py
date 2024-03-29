def getmaxdivisor(num):
    if num==1:
        return 0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            if num//i>10000000:
                continue
            return num//i
    
    return 1

def solution(begin, end):
    answer = []
    for num in range(begin,end+1):
        answer.append(getmaxdivisor(num))
    
    return answer