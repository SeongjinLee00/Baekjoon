T=int(input())

for _ in range(T):
    numbers = list(map(int,input().split()))
    m=9999999999999999999998
    a=0
    
    for number in numbers:
        if not number%2:
            m=min(number,m)
            a+=number
    print(a,m)