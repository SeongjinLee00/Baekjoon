def solution(s):
    l=[]
    i=0
    d={'S':1, 'D':2, 'T':3}
    while True:
        if s[i].isnumeric():
            i+=2
            while i<len(s) and not s[i].isnumeric():
                i+=1
        l.append(i)
        if i>=len(s):
            break
    l.pop()
    
    a=s[0:l[0]]
    b=s[l[0]:l[1]]
    c=s[l[1]:]
    
    ret=[0,0,0]
    
    if a[0]+a[1]=='10':
        ret[0]=(10**d[a[2]])
        if len(a)==4:
            if a[3]=='*':
                ret[0]*=2
            elif a[3]=='#':
                ret[0]*=(-1)
    else:
        ret[0]=(int(a[0])**d[a[1]])
        if len(a)==3:
            if a[2]=='*':
                ret[0]*=2
            elif a[2]=='#':
                ret[0]*=(-1)
    
    if b[0]+b[1]=='10':
        ret[1]=(10**d[b[2]])
        if len(b)==4:
            if b[3]=='*':
                ret[0]*=2
                ret[1]*=2
            elif a[3]=='#':
                ret[1]*=(-1)
    else:
        ret[1]=(int(b[0])**d[b[1]])
        if len(b)==3:
            if b[2]=='*':
                ret[0]*=2
                ret[1]*=2
            elif b[2]=='#':
                ret[1]*=(-1)
    
    if c[0]+c[1]=='10':
        ret[2]=(10**d[c[2]])
        if len(c)==4:
            if c[3]=='*':
                ret[1]*=2
                ret[2]*=2
            elif c[3]=='#':
                ret[2]*=(-1)
    else:
        ret[2]=(int(c[0])**d[c[1]])
        if len(c)==3:
            if c[2]=='*':
                ret[1]*=2
                ret[2]*=2
            elif c[2]=='#':
                ret[2]*=(-1)
    
    return sum(ret)