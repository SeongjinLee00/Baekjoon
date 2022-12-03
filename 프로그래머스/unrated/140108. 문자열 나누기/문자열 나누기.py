def solution(s):
    ans=0
    if len(s)==1:
        return 1
    i=0
    cnt1=0
    cnt2=0
    now=s[0]
    while True:
        if s[i]==now:
            cnt1+=1
        else:
            cnt2+=1
        i+=1
        if cnt1==cnt2:
            ans+=1
            cnt1=0
            cnt2=0
            now=s[i]
        if i==len(s)-1:
            break
    return ans+1