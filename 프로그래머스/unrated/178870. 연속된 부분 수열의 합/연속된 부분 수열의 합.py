def solution(sequence, k):
    l=0
    r=1
    
    s=sequence[0]+sequence[1]
    c=[]
    
    if k==sequence[0]:
        return([0,0])
    
    while True:
        if s>k:
            s-=sequence[l]
            l+=1
        elif s<k:
            r+=1
            if r==len(sequence):
                break
            s+=sequence[r]
        else:
            c.append([l,r])
            s-=sequence[l]
            l+=1
            r+=1
            if r==len(sequence):
                break
            s+=sequence[r]
        
    c.sort(key=lambda x:(x[1]-x[0],x[0]))

    return c[0]