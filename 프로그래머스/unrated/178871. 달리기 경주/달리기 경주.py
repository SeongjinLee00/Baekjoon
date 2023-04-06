def solution(players, callings):
    d1=dict()
    d2=dict()
    for idx,name in enumerate(players):
        d1[name]=idx
        d2[idx]=name
        
    for call in callings:
        me_name=call
        me_rank=d1[call]
        other_name=d2[me_rank-1]
        other_rank=me_rank-1
        
        d1[other_name]+=1
        d2[me_rank]=other_name
        d1[me_name]-=1
        d2[other_rank]=me_name
    
    ans=[0]*len(players)
    
    for name,rank in d1.items():
        ans[rank]=name
    
    return ans