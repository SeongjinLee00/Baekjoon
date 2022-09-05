def solution(d, budget):
    d.sort()
    
    cnt=0
    for dd in d:
        budget-=dd
        if budget>=0:
            cnt+=1
        else:
            return cnt
    return cnt