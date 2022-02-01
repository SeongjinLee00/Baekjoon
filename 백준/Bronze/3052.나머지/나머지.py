numbers=[]

for i in range(10):
    numbers.append(int(input()))

remainders=[]

for j in range(len(numbers)):
    remainders.append(numbers[j]%42)

remainders=set(remainders)

print(len(remainders))