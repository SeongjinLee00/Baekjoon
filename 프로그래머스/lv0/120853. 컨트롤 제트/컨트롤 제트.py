def solution(s):
    s=s.split()
    
    disabled=[0]*len(s)
    
    ans=0
    for idx,val in enumerate(s):
        if val=='Z':
            if idx==0:
                continue
            prev=1
            while disabled[idx-prev]==1 or s[idx-prev]=='Z':
                prev+=1
            ans-=int(s[idx-prev])
            disabled[idx-prev]=1
        else:
            ans+=int(val)
    
    return ans