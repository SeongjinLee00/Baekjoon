while True:
    numbers=list(map(int,input().split()))

    c=max(numbers)**2
    numbers.remove(max(numbers))

    a=numbers[0]**2
    b=numbers[1]**2

    if max(numbers)==0:
        break
    else:
        if a+b==c:
            print('right')
        else:
            print('wrong')