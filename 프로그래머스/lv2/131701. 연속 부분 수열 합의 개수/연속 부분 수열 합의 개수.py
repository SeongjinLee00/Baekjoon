def solution(elements):
    b=len(elements)
    elements*=2
    s=set()
    print(elements)
    for i in range(len(elements)-1):
        tmp=elements[i]
        s.add(tmp)
        for j in range(i+1,min(i+b,len(elements))):
            tmp+=elements[j]
            s.add(tmp)
    
    return len(s)