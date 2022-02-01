N=int(input())

def is_group(s):
    for i in range(len(s)):
        if s.count(s[i])>=2 and s.count(s[i]*(s.count(s[i])))==0:
            return False
    return True
count=0
for i in range(N):
    word=input()
    if is_group(word)==True:
        count+=1

print(count)