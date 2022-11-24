from collections import defaultdict

def solution(lines):
    d=defaultdict(int)
    
    for num in range(lines[0][0],lines[0][1]):
        d[num+0.5]+=1
    for num in range(lines[1][0],lines[1][1]):
        d[num+0.5]+=1
    for num in range(lines[2][0],lines[2][1]):
        d[num+0.5]+=1
    
    ret=0
    
    for v in d.values():
        if v>=2:
            ret+=1
    
    return ret