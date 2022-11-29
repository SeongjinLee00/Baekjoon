from collections import defaultdict
from heapq import heappop,heappush

def solution(alp, cop, problems):
    distances=defaultdict(lambda: float('inf'))
    graphs={(1,0,0):1, (0,1,1):1}
    reqs={(1,0,0):(0,0), (0,1,1):(0,0)}
    
    alp_goal=-1
    cop_goal=-1
    
    dummy=1
    
    for a,b,c,d,e in problems:
        dummy+=1
        alp_goal=max(alp_goal,a)
        cop_goal=max(cop_goal,b)
        
        if c+d>e:
            # if (c,d) in reqs:
            #     alp_req,cop_req=reqs[(c,d)]
            #     cost=graphs[(c,d)]
            #     if alp_req<c and cop_req<d and cost<e:
            #         continue
            graphs[(c,d,dummy)]=e
            reqs[(c,d,dummy)]=(a,b)
    
    q=[(0,alp,cop)]
    distances[(alp,cop)]=0
    
    while q:
        d,alp,cop=heappop(q)
        alp=min(alp_goal,alp)
        cop=min(cop_goal,cop)
        
        if alp>=alp_goal and cop>=cop_goal:
            return d
        
        if distances[(alp,cop)]<d:
            continue
        
        for alp_rwd,cop_rwd,dummy in graphs:
            alp_req,cop_req=reqs[(alp_rwd,cop_rwd,dummy)]
            if alp<alp_req or cop<cop_req:
                continue
                
            next_distance=d+graphs[(alp_rwd,cop_rwd,dummy)]
            if next_distance<distances[(alp+alp_rwd,cop+cop_rwd)]:
                distances[(alp+alp_rwd,cop+cop_rwd)]=next_distance
                heappush(q,[next_distance,alp+alp_rwd,cop+cop_rwd])
        