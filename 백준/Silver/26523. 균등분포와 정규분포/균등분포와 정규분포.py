import sys

input = sys.stdin.readline

T=100

for tc in range(T):
    mid=0
    tail=0

    for _ in range(5000):
        num=float(input())

        if 0.25<num<0.75:
            mid+=1
        else:
            tail+=1
    
    if 0.9*mid<tail<1.1*mid:
        print('A')
    else:
        print('B')