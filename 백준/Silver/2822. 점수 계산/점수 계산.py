numbers=[]

for i in range(8):
    numbers.append([int(input()),i+1])

numbers.sort()
numbers=numbers[3:]

ans=0
idx=[]

for score,i in numbers:
    ans+=score
    idx.append(str(i))

idx.sort()
print(ans)
print(" ".join(idx))