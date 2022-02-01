M=int(input())
N=int(input())

numbers=[number for number in range(M,N+1)]

for number in range(M,N+1):
    for i in range(2,number//2+1):
        if number%i==0:
            numbers.remove(number)
            break
if 1 in numbers:
    numbers.remove(1)

if len(numbers)==0:
    print(-1)

else:

    print(sum(numbers))
    print(min(numbers))