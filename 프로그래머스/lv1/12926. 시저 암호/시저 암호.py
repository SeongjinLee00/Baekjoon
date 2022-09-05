def solution(s, n):
    answer = ''
    
    for c in s:
        if c==' ':
            answer+=c
            continue
        if 'a'<=c<='z' and chr(ord(c)+n)>'z':
            answer+=chr(ord(c)+n-26)
            continue
        if 'A'<=c<='Z' and chr(ord(c)+n)>'Z':
            answer+=chr(ord(c)+n-26)
            continue
        answer+=chr(ord(c)+n)
    
    return answer