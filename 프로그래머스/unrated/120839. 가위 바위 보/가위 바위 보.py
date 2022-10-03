def solution(rsp):
    answer = ''
    for c in rsp:
        if c=='0':
            answer+='5'
        elif c=='2':
            answer+='0'
        else:
            answer+='2'
    return answer