S=input()

stack=''

answer=''

i=0
while True:
    if S[i]=='<':
        answer+=stack[::-1]
        stack=''
        answer+=S[i]
        i+=1
        while S[i]!='>':
            answer+=S[i]
            i+=1
        answer+='>'
        i+=1
         
    elif S[i]==' ':
        answer+=stack[::-1]
        stack=''
        answer+=' '
        i+=1
    else:
        stack+=S[i]
        i+=1

    if i==len(S):
        break

if stack:
    answer+=stack[::-1]

print(answer)