n=int(input())

if n==1:
    print(1)
elif n<=3:
    print(2)
elif n<=6:
    print(3)
elif n<=10:
    print(4)
elif n<=15:
    print(5)
elif n<=21:
    print(6)
elif n<=28:
    print(7)
else:
    print(n//7+bool(n%7)+3)