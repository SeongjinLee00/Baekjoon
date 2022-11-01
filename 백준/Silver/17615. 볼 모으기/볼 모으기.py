N=int(input())
s=input()

r=[]
b=[]

i=0
while True:
    now=s[i]
    cnt=1
    while i<N-1 and s[i+1]==now:
        i+=1
        cnt+=1
    if now=='R':
        r.append(cnt)
    else:
        b.append(cnt)
    
    if i==N-1:
        break

    i+=1

rr=0
bb=0

rr=sum(r)

bb=sum(b)

if not r or not b:
    print(0)
    exit(0)

if s[0]=='R' and (r[0]>=r[-1] or s[N-1]=='B'):
    rr-=r[0]
elif s[N-1]=='R' and (r[0]<=r[-1] or s[0]=='B'):
    rr-=r[-1]

if s[0]=='B' and (b[0]>=b[-1] or s[N-1]=='R'):
    bb-=b[0]
elif s[N-1]=='B' and (b[0]<=b[-1] or s[0]=='R'):
    bb-=b[-1]

print(min(rr,bb))