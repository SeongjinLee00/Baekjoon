s=input()
S=set()

for k in range(1,len(s)+1):
    for l in range(len(s)):
        if l+k<=len(s):
            S.add(s[l:l+k])
        else:
            break

print(len(S))