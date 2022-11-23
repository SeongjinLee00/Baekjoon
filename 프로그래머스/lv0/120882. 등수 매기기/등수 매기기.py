def solution(score):
    ref1=[]
    ret=[0]*len(score)
    for a,b in score:
        ref1.append(a+b)
    
    ref1.sort(reverse=True)
    
    rank=dict()
    
    cnt=1
    
    for val in ref1:
        if val in rank:
            cnt+=1
            continue
        else:
            rank[val]=cnt
            cnt+=1
    
    for idx,val in enumerate(score):
        ret[idx]=rank[sum(val)]
    
    return ret