from collections import deque

def solution(order):
    truck=[0]
    stack=[0]
    belt=deque([i+1 for i in range(len(order))])
    
    i=0
    while True:
        now=order[i]

        if belt and belt[0]==now:
            truck.append(belt.popleft())
            i+=1
        elif stack and stack[-1]==now:
            truck.append(stack.pop())
            i+=1
        else:
            stack.append(belt.popleft())
        
        if not belt:
            now=order[i]
            while stack and stack[-1]==now:
                truck.append(stack.pop())
                i+=1
                if i==len(order):
                    return len(order)
                now=order[i]
            
            return len(truck)-1