def solution(n, words):
    s=set([words[0]])
    
    cnt=1
    for i in range(1,len(words)):
        cnt+=1

        if words[i] in s:
            print(cnt)
            return [(cnt-1)%n+1,(cnt+(n-1))//n]
        if words[i][0]!= words[i-1][-1]:
            print(cnt)
            return [(cnt-1)%n+1,(cnt+(n-1))//n]
        s.add(words[i])
    
    return [0,0]