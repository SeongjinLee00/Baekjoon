from itertools import permutations
innings=int(input())
players=[]

for _ in range(innings):
    players.append(list(map(int,input().split())))

numbers=[1,2,3,4,5,6,7,8]
perm=permutations(numbers,8)

maxscore=0
for item in perm: # 40320
    score=0

    order=list(item)[0:3]+[0]+list(item)[3:8]
    hit=[0,0,0,0,0,0,0,0,0]

    nth=0
    for inning in range(innings): # 50
        out=0
        for i in range(9):
            hit[i]=players[inning][order[i]]

        base0=0
        base1=0
        base2=0
        while out<3:
            nth=nth%9
            if hit[nth]==0:
                out+=1
            elif hit[nth]==1:
                if base2:
                    score+=1
                    base2=0
                if base1:
                    base2=1
                    base1=0
                if base0:
                    base1=1

                base0=1
            elif hit[nth]==2:
                if base2:
                    score+=1
                    base2=0
                if base1:
                    score+=1

                if base0:
                    base2=1
                    base0=0
                base1=1
            elif hit[nth]==3:
                if base2:
                    score+=1

                if base1:
                    score+=1
                    base1=0
                if base0:
                    score+=1
                    base0=0
                base2=1
            elif hit[nth]==4:
                score+=(base0+base1+base2+1)
                base0=0
                base1=0
                base2=0

            nth+=1
    if score>maxscore:
        maxscore=score

print(maxscore)