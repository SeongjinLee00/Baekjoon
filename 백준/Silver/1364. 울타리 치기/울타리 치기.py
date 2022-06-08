N=int(input())
answer=0
x=0
for i in range(N+1):
    if i%6==1:
        answer-=1
    elif i%6==0:
        x+=1
    answer+=x

print(answer)