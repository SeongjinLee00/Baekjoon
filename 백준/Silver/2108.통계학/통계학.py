N=int(input())

numbers=[]
for _ in range(N):
    numbers.append(int(input()))

numbers.sort()

mean=round(sum(numbers)/len(numbers))
median=numbers[N//2]
width=max(numbers)-min(numbers)

counts=[0]*8001
for number in numbers:
    counts[number+4000] +=1

frequent=[]
for i in range(len(counts)):
    if counts[i]==max(counts):
        frequent.append(i-4000)
mostfrequent=0
if len(frequent)>1:
    mostfrequent=frequent[1]
elif len(frequent)==1:
    mostfrequent=frequent[0]

print(mean)
print(median)
print(mostfrequent)
print(width)