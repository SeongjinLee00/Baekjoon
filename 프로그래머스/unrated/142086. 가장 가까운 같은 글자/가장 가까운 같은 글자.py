def solution(s):
    d=dict()
    
    result=[]
    
    for i,c in enumerate(s):
        if c not in d:
            result.append(-1)
            d[c]=i
        else:
            result.append(i-d[c])
            d[c]=i
    
    return result