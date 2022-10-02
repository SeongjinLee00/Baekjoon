def solution(my_string):
    answer = ''
    s={'a','e','i','o','u'}
    
    for c in my_string:
        if c not in s:
            answer+=c
            
    return answer