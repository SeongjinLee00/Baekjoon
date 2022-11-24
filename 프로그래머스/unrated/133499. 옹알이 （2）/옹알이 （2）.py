def solution(babbling):
    p={'A','B','C','D'}
    
    ans=0
    
    for word in babbling:
        word=word.replace('aya','A')
        word=word.replace('ye','B')
        word=word.replace('woo','C')
        word=word.replace('ma','D')
        
        stack=[]
        
        for c in word:
            if c not in p:
                break
            if not stack:
                stack.append(c)
            else:
                if c==stack[-1]:
                    break
                else:
                    stack.append(c)
        else:
            ans+=1
    
    return ans