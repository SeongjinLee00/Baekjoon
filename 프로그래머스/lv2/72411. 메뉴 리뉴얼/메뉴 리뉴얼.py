from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    d=defaultdict(int)
    
    for order in orders:
        for num in course:
            if num>len(order):
                break
            for item in combinations(order,num):
                d[tuple(sorted(item))]+=1
                
    candidates=defaultdict(list)
    for k,v in d.items():
        if len(k)<2 or v<2:
            continue
        if not candidates[len(k)]:
            candidates[len(k)].append((k,v))
        else:
            if candidates[len(k)][0][1]==v:
                candidates[len(k)].append((k,v))
            elif candidates[len(k)][0][1]<v:
                candidates[len(k)]=[(k,v)]
    
    result=[]
    
    for item in candidates.values():
        for s,i in item:
            result.append("".join(s))
    
    return sorted(result)