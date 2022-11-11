def solution(s):
    answer = []
    i=1
    
    while i<len(s):
        if s[i]=='{':
            tmp=set()
            tmp2=''
            i+=1
            while s[i]!='}':
                if s[i]==',':
                    tmp.add(int(tmp2))
                    tmp2=''
                    i+=1
                tmp2+=s[i]
                i+=1
            tmp.add(int(tmp2))
            answer.append(tmp)
        i+=1
    
    ret=[0]*len(answer)
    answer.sort(key=lambda x:len(x))
    visited=set()
    cnt=0
    for item in answer:
        for i in item:
            if i not in visited:
                ret[cnt]=i
                cnt+=1
                visited.add(i)
    
    return ret