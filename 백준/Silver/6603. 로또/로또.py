from itertools import combinations

while True:
    N,*S=map(int,input().split())
    if not S:
        exit(0)

    for item in combinations(S,6):
        print(*item)
    
    print()