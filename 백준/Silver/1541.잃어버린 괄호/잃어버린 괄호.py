string=input()

numbers=[]
temp=''
for i in range(len(string)-1): # 파싱 이것보다 쉽게 할 수 있을것같은데...
    temp+=string[i]
    if string[i+1]=='+' or string[i+1]=='-':
        numbers.append(temp)
        temp=''
numbers.append(temp)
numbers[-1]+=string[-1]

numbers=list(map(int,numbers))
absnumbers=list(map(abs,numbers))

sums=0
idx=len(numbers)
for i in range(len(numbers)):
    if numbers[i]<0:
        idx=i
        break

sums=sum(numbers[:idx])-sum(absnumbers[idx:])
print(sums)