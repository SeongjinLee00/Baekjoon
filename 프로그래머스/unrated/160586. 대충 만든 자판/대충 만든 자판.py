def solution(keymap, targets):
    d=dict()
    
    for key in keymap:
        for i in range(len(key)):
            if key[i] not in d:
                d[key[i]]=i+1
            else:
                d[key[i]]=min((i+1),d[key[i]])
    
    ret = []
    
    for target in targets:
        ans=0
        for letter in target:
            if letter not in d:
                ans=-1
                break
            ans+=d[letter]
        ret.append(ans)
    
    return ret