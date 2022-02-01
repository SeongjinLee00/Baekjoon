numbers=[]

for i in range(3):
    numbers.append(int(input()))

product=numbers[0]*numbers[1]*numbers[2]

count=0
for j in range(10):
    for i in range(len(str(product))):
        if str(product)[i]==str(j):
            count=count+1

    print(count)
    count=0