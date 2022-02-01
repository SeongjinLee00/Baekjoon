s=list(input())

lst=[-1 for i in range(26)]

idx=0
archieve=[]
for i in range(97,123):
    for j in range(len(s)):
        if chr(i)==s[j] and chr(i) not in archieve:
            lst[i-97]=j
            archieve.append(chr(i))

for i in range(len(lst)):
    print(lst[i], end=' ')