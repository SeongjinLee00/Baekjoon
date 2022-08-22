from collections import deque

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    s1=sum(queue1)
    s2=sum(queue2)
    ans=0
    
    N=len(queue1)

    while True:
        if ans>3*N:
            return -1
        ans+=1
        if s1>s2:
            queue2.append(queue1.popleft())
            s1-=queue2[-1]
            s2+=queue2[-1]
        elif s1<s2:
            queue1.append(queue2.popleft())
            s1+=queue1[-1]
            s2-=queue1[-1]
        else:
            return ans-1