import copy

N=int(input())

dices=[]
sums=[]
for _ in range(N):
    dices.append(list(map(int,input().split())))

tempdices=copy.deepcopy(dices)

base=dices[0][0]
top=dices[0][5]

dices[0].remove(base)
dices[0].remove(top)

for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

dices=copy.deepcopy(tempdices)

base=dices[0][1]
top=dices[0][3]
dices[0].remove(base)
dices[0].remove(top)
for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

dices=copy.deepcopy(tempdices)

base=dices[0][2]
top=dices[0][4]
dices[0].remove(base)
dices[0].remove(top)
for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

dices=copy.deepcopy(tempdices)

base=dices[0][3]
top=dices[0][1]
dices[0].remove(base)
dices[0].remove(top)
for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

dices=copy.deepcopy(tempdices)

base=dices[0][4]
top=dices[0][2]
dices[0].remove(base)
dices[0].remove(top)
for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

dices=copy.deepcopy(tempdices)

base=dices[0][5]
top=dices[0][0]
dices[0].remove(base)
dices[0].remove(top)
for j in range(1,N):
    if dices[j].index(top)==0:
        top=dices[j][5]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

    elif dices[j].index(top)==1:
        top=dices[j][3]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==2:
        top=dices[j][4]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==3:
        top=dices[j][1]
        dices[j].remove(dices[j][3])
        dices[j].remove(dices[j][1])

    elif dices[j].index(top)==4:
        top=dices[j][2]
        dices[j].remove(dices[j][4])
        dices[j].remove(dices[j][2])

    elif dices[j].index(top)==5:
        top=dices[j][0]
        dices[j].remove(dices[j][5])
        dices[j].remove(dices[j][0])

sums.append(sum(map(max,dices)))

print(max(sums))