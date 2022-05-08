from heapq import heappop, heappush, heapify

def solution(operations):
    max_heap=[]
    min_heap=[]

    idx=0
    visited=[0]*1000001
    for operation in operations:
        s,num=operation.split()
        num=int(num)

        if s=='I':
            heappush(min_heap,(num,idx))
            heappush(max_heap,(-num,idx))
            visited[idx]=1
        
        elif s=='D':
            if num==1:
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]]=0
                    heappop(max_heap)
            elif num==-1:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]]=0
                    heappop(min_heap)

        idx+=1
    while max_heap and not visited[max_heap[0][1]]:
        heappop(max_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heappop(min_heap)

    if max_heap and min_heap:
        return str(-max_heap[0][0])+' '+str(min_heap[0][0])
    else:
        return 'EMPTY'

T=int(input())

import sys
input=sys.stdin.readline

for _ in range(T):
    k=int(input())
    operations=[]

    for _ in range(k):
        operations.append(input())

    print(solution(operations))