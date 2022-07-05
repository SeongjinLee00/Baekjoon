from collections import defaultdict

S=input()

dd=defaultdict(int)

for c in S:
    dd[c]+=1

odd=0
for key,value in dd.items():
    if value%2:
        odd+=1

if odd>=2:
    print("I'm Sorry Hansoo")
    exit(0)

ans=['']*len(S)

cnt=0
for number in range(65,65+26):
    if chr(number) in dd:
        tmp=dd[chr(number)]
        for i in range(cnt//2,cnt//2+tmp//2):
            ans[i]=chr(number)
            ans[len(S)-1-i]=chr(number)
        cnt+=tmp
        if tmp%2:
            ans[len(S)//2]=chr(number)

print("".join(ans))