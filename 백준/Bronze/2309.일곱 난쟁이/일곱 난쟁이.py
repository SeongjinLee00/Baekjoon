dwarves=[]

for i in range(9):
    dwarves.append(int(input()))

remainder=sum(dwarves)-100

for j in range(9):
    for k in range(9):
        if dwarves[j]+dwarves[k]==remainder:
            remainder1=dwarves[j]
            remainder2=dwarves[k]

dwarves.remove(remainder1)
dwarves.remove(remainder2)

dwarves.sort()

for dwarf in dwarves:
    print(dwarf)