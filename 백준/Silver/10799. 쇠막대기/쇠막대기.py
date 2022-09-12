p=input()

c=0
a=0
i=0
while i<len(p):
    if p[i]=='(':
        if p[i+1]==')':
            a+=c
            i+=1
        else:
            c+=1
    else:
        c-=1
        a+=1
    i+=1

print(a)