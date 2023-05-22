def solution(a):
    mIdx=a.index(min(a))
    
    tmp_min=a[0]
    cnt=0
    for l in range(mIdx):
        tmp_min=min(tmp_min,a[l])
        if a[l]<=tmp_min:
            cnt+=1
            
    tmp_min=a[len(a)-1]
    for r in range(len(a)-1,mIdx,-1):
        tmp_min=min(tmp_min,a[r])
        if a[r]<=tmp_min:
            cnt+=1
    
    return cnt+1