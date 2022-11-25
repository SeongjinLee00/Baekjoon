from heapq import heappop, heappush

def solution(k, score):
    pq = []
    
    ret = []
    
    for num in score:
        heappush(pq,num)
        if len(pq)>k:
            heappop(pq)
        ret+=[pq[0]]
    
    return ret