S,P=map(int,input().split())

password=input()

A,C,G,T=map(int,input().split())

ans=0

i=0
j=P

a=password[i:j].count('A')
c=password[i:j].count('C')
g=password[i:j].count('G')
t=password[i:j].count('T')

while True:
    if a>=A and c>=C and g>=G and t>=T:
        ans+=1
    if j==S:
        print(ans)
        exit(0)
    if password[i]=='A':
        a-=1
    elif password[i]=='C':
        c-=1
    elif password[i]=='G':
        g-=1
    elif password[i]=='T':
        t-=1
    
    i+=1

    if password[j]=='A':
        a+=1
    elif password[j]=='C':
        c+=1
    elif password[j]=='G':
        g+=1
    elif password[j]=='T':
        t+=1
    j+=1