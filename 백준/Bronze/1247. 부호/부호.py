import sys

input = sys.stdin.readline

for _ in range(3):
    tmp=0
    N=int(input())

    for _ in range(N):
        tmp+=int(input())

    if tmp>0:
        print('+')
    elif tmp<0:
        print('-')
    else:
        print('0')