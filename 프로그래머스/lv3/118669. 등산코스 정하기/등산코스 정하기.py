from heapq import heappop,heappush

def solution(n, paths, gates, summits):
    intensities=[float('inf')]*(n+1)
    graph=[[] for _ in range(n+1)]
    
    summits_set=set(summits)
    
    for s,e,c in paths:
        graph[s].append([c,e])
        graph[e].append([c,s])
    
    q=[]
    
    for gate in gates:
        q.append([0,gate,False])
        intensities[gate]=0
    
    ans=float('inf')
    candidates=[]
    while q:
        d,now,found_summit=heappop(q)
        
        if found_summit:
            continue
            
        if d>ans:
            break
        
        if intensities[now]<d:
            continue

        if now in summits_set:
            ans=d
            candidates.append(now)
            found_summit=True
        
        for intensity,next in graph[now]:
            next_d=max(d,intensity)
            
            if next_d<intensities[next]:
                intensities[next]=next_d
                heappush(q,[next_d,next,found_summit])
    
    return [min(candidates), ans]