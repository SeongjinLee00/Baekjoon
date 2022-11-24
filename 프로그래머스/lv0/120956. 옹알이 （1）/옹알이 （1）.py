from itertools import permutations

def solution(babbling):
    p={'aya','ye','woo','ma'}
    
    possibles=set()
    
    for k in range(1,5):
        perm=permutations(p,k)
        for item in perm:
            possibles.add("".join(item))
    
    ans=0
    
    for word in babbling:
        if word in possibles:
            ans+=1
    
    return ans