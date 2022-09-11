from collections import defaultdict

def solution(N, stages):
    challenge=defaultdict(int)
    
    for number in stages:
        for ex in range(1,number+1):
            challenge[ex]+=1
    
    ret=[]
    for stage in range(1,N+1):
        if challenge[stage]==0:
            fail=0
        else:
            fail=(challenge[stage]-challenge[stage+1])/challenge[stage]

        ret.append([fail,stage])
        
    ret.sort(key=lambda x:-x[0])
    
    ret2=[]
    
    for item in ret:
        ret2.append(item[1])
        
    return ret2