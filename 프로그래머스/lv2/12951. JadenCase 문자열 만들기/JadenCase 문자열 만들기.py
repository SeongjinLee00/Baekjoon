def solution(s):
    s=s.title()
    
    ans=s[0]
    for i in range(1,len(s)):
        if s[i-1].isnumeric() and s[i].isupper():
            ans+=s[i].lower()
        else:
            ans+=s[i]
    
    return ans