from collections import defaultdict

def solution(want, number, discount):
    d=defaultdict(int)
    
    for i in range(len(want)):
        d[want[i]]=number[i]
    
    dd=defaultdict(int)
    for i in range(10):
        dd[discount[i]]+=1
    
    ans=int(d==dd)

    for x in range(10,len(discount)):
        dd[discount[x-10]]-=1
        if dd[discount[x-10]]==0:
            dd.pop(discount[x-10])
        dd[discount[x]]+=1

        ans+=int(d==dd)
    
    return ans