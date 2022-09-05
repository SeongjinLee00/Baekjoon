from bisect import bisect_left

def solution(citations):
    citations.sort()
    N=len(citations)
    for h in range(1,1001):
        if N-bisect_left(citations,h)<h:
            return h-1