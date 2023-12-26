from heapq import heappop, heappush

def solution(book_time):
    new_list = []
    for s,e in book_time:
        m1,s1 = map(int,s.split(':'))
        m2,s2 = map(int,e.split(':'))
        new_list.append([m1*60+s1, m2*60+s2+10])
    
    new_list.sort(key=lambda x:x[0])
    
    pq=[]
    
    ans=0
    
    for s,e in new_list:
        while pq and pq[0]<=s:
            heappop(pq)
        heappush(pq,e)
        ans=max(ans,len(pq))
    
    return ans