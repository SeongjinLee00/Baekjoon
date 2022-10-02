from collections import Counter

def solution(s):
    c=Counter(s)
    
    ret=[]
    for k,v in c.items():
        if v==1:
            ret.append(k)
    
    return "".join(sorted(ret))