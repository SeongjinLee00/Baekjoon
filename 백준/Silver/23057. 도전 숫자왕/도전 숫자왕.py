N=int(input())
numbers=list(map(int,input().split()))

possibles=set()

for number in numbers:

    for p in set(possibles):
        possibles.add(p+number)
    possibles.add(number)

print(sum(numbers)-len(possibles))