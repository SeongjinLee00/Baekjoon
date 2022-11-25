n=int(input())

if n%8 in [1,2,3,4,5]:
    print(n%8)
else:
    if n%8==0:
        print(2)
    elif n%8==7:
        print(3)
    elif n%8==6:
        print(4)