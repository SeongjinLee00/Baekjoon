print('Gnomes:')
T=int(input())
for _ in range(T):
    numbers=list(map(int,input().split()))
    if sorted(numbers)==numbers or sorted(numbers)==numbers[::-1]:
        print('Ordered')
    else:
        print('Unordered')