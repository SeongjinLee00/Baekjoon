from collections import defaultdict
from heapq import heappop, heappush

def solution(k, tangerine):
    d=defaultdict(int)
    
    for num in tangerine:
        d[num]+=1
    
    pq=[]
    
    for v in d.values():
        heappush(pq,-v)
    
    now=0
    cnt=0
    while True:
        now-=heappop(pq)
        cnt+=1
        
        if now>=k:
            return cnt