def solution(s):
    answer = ''
    tmp=1
    for c in s:
        if c==' ':
            tmp=1
            answer+=c
            continue
        elif tmp%2:
            answer+=(c.upper())
        else:
            answer+=(c.lower())
        tmp+=1
    
    return answer