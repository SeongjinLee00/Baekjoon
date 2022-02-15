from collections import deque

N,M=map(int,input().split())

queue=deque(x for x in range(1,N+1)) # [1,2,3,4,5,6,7,8,9,10]
numbers=deque(map(int,input().split())) # [2,9,5]

i=0
cnt=0
cnt2=0

while True:
    if numbers[i]==queue[0]:
        i+=1
        queue.popleft()
        cnt2+=1
        if cnt2==M:
            print(cnt)
            exit(0)
    else:
        if queue.index(numbers[i])<=len(queue)//2:
            while True:
                queue.rotate(-1)
                cnt+=1
                if queue[0]==numbers[i]:
                    break
        elif queue.index(numbers[i])>len(queue)//2:
            while True:
                queue.rotate(1)
                cnt+=1
                if queue[0]==numbers[i]:
                    break