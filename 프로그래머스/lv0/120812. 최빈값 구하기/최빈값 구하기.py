from collections import defaultdict

def solution(array):
    d=defaultdict(int)
    
    M=-1
    for v in array:
        d[v]+=1
        M=max(M,d[v])
    
    ret=-1
    flag=False
    for k,v in d.items():
        if v==M:
            if flag:
                return -1
            ret=k
            flag=True
    
    return ret