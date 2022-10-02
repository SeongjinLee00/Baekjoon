from collections import deque

def solution(s):
    ans=0
    def check(s):
        stack=[]
        
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c==')':
                    if stack[-1]!='(':
                        return False
                    else:
                        stack.pop()
                elif c=='}':
                    if stack[-1]!='{':
                        return False
                    else:
                        stack.pop()
                elif c==']':
                    if stack[-1]!='[':
                        return False
                    else:
                        stack.pop()
        
        return not bool(stack)
    
    s=deque(s)
    ans=0
    for i in range(len(s)):
        s.rotate(1)

        ans+=check(s)
    
    return ans