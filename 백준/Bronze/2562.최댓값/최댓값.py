numbers=[]

for i in range(9):
    numbers.append(int(input()))

print(max(numbers))

for j in range(len(numbers)):
    if numbers[j]==max(numbers):
        print(j+1)