from collections import deque,Counter

def solution(topping):
    leftset=set()
    
    right=deque(topping)
    rightdict=Counter(right)
    cnt=0
    
    while True:
        now=right.popleft()
        leftset.add(now)
        rightdict[now]-=1
        
        if rightdict[now]==0:
            rightdict.pop(now)

        if len(leftset)==len(rightdict):
            cnt+=1
        
        if len(leftset)>len(rightdict):
            return cnt