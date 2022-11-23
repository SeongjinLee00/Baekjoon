def solution(emergency):
    d=dict()
    reference=sorted(emergency)
    
    for i,v in enumerate(reference):
        d[v]=len(emergency)-i
    
    result=[0]*len(emergency)
    
    for i in range(len(emergency)):
        result[i]=d[emergency[i]]
    
    return result