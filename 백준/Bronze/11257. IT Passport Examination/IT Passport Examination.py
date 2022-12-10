N=int(input())

for _ in range(N):
    a,b,c,d=map(int,input().split())
    result='PASS'
    if b<10.5:
        result='FAIL'
    elif c<7.5:
        result='FAIL'
    elif d<12:
        result='FAIL'
    elif b+c+d<55:
        result='FAIL'
    
    print(f'{a} {b+c+d} {result}')