from heapq import heappop, heappush, heapify

def solution(n, works):
    answer = 0
    S=sum(works)
    
    if S<=n:
        return 0
    
    pq=[]
    
    for work in works:
        heappush(pq,-work)
    
    for _ in range(n):
        heappush(pq,heappop(pq)+1)
        
    for num in pq:
        answer+=(num*num)
    
    return answer