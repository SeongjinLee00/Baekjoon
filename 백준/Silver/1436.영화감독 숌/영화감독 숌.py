N=int(input())

numbers=[str(x) for x in range(1000,2700000)]
devilnumbers=[]
for i in range(len(numbers)):
    for j in range(len(numbers[i])-2):
        if numbers[i][j]=='6' and numbers[i][j+1]=='6' and numbers[i][j+2]=='6':
            devilnumbers.append(int(numbers[i]))
            break

devilnumbers.append(666)
devilnumbers.sort()

print(devilnumbers[N-1])