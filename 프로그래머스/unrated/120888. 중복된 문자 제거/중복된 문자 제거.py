def solution(my_string):
    s=set()
    
    ret=''

    for c in my_string:
        if c not in s:
            ret+=c
            s.add(c)
            
    return ret