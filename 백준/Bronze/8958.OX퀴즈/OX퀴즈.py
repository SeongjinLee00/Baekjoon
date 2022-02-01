T=int(input())

for _ in range(T):
    ox=input()
    scores=[]

    for i in range(len(ox)):
        if ox[i]=='O' and i==0:
            scores.append(1)
        elif ox[i]=='O':
            scores.append(scores[i-1]+1)
        elif ox[i]=='X':
            scores.append(0)

    print(sum(scores))