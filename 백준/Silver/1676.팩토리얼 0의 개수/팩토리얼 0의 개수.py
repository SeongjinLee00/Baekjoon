N=int(input())

two=0
five=0

for i in range(2,N+1):
    while i%2==0 or i%5==0:
        if i%2==0:
            i=i//2
            two += 1
        if i%5==0:
            i=i//5
            five += 1

print(five)