import sys
input=sys.stdin.readline

T=int(input())

for _ in range(T):
    N=int(input())
    flag=0

    numbers=[]

    for _ in range(N):
        numbers.append(input().rstrip())

    numbers.sort()

    numbers_set=set()

    for number in numbers:
        s=''
        if flag:
            break
        for n in number:
            s+=n
            if s in numbers_set:
                print('NO')
                flag=1
                break
        numbers_set.add(s)
    if not flag:
        print('YES')