from collections import defaultdict

def solution(id_list, report, k):
    d=defaultdict(int)
    report=list(set(list(report)))
    
    for r in report:
        s,e=r.split()
        d[e]+=1
    
    names=dict()
    
    i=0
    for name in id_list:
        names[name]=i
        i+=1
    
    ret=[0]*len(id_list)
    
    for r in report:
        s,e=r.split()
        if d[e]>=k:
            ret[names[s]]+=1
    
    return ret