from collections import defaultdict

R,C=map(int,input().split())

board=[]

for _ in range(R):
    board.append(list(input()))

dr=[9999,1,1,1,0,0,0,-1,-1,-1]
dc=[9999,-1,0,1,-1,0,1,-1,0,1]

jongsu=[0,0]
arduinos=defaultdict(int)
for i in range(R):
    for j in range(C):
        if board[i][j]=='I':
            jongsu=[i,j]
        if board[i][j]=='R':
            arduinos[(i,j)]+=1

commands=input()

for t in range(len(commands)):
    c=int(commands[t])
    jongsu[0]+=dr[c]
    jongsu[1]+=dc[c]

    if (jongsu[0],jongsu[1]) in arduinos:
        print(f'kraj {t+1}')
        exit(0)

    for i,j in list(arduinos.keys()):
        arduinos[(i,j)]-=1
        if jongsu[0]>i and jongsu[1]>j:
            direction=3
        elif jongsu[0]<i and jongsu[1]>j:
            direction=9
        elif jongsu[0]>i and jongsu[1]<j:
            direction=1
        elif jongsu[0]<i and jongsu[1]<j:
            direction=7
        elif jongsu[0]==i and jongsu[1]>j:
            direction=6
        elif jongsu[0]==i and jongsu[1]<j:
            direction=4
        elif jongsu[0]>i and jongsu[1]==j:
            direction=2
        elif jongsu[0]<i and jongsu[1]==j:
            direction=8
    
        i+=dr[direction]
        j+=dc[direction]

        arduinos[(i,j)]+=1

        if [i,j]==jongsu:
            print(f'kraj {t+1}')
            exit(0)

    for k,v in list(arduinos.items()):
        if v==0 or v>=2:
            arduinos.pop(k)

answer=[['.']*C for _ in range(R)]

for i,j in arduinos:
    answer[i][j]='R'
answer[jongsu[0]][jongsu[1]]='I'

for row in answer:
    print("".join(row))