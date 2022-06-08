N=int(input())

numbers=list(map(int,input().split()))

if N==1:
    print('A')
    exit(0)
elif N==2:
    if numbers[0]==numbers[1]:
        print(numbers[0])
    else:
        print('A')
    exit(0)
else:
    if numbers[1]==numbers[0]:
        if numbers[2]==numbers[1] and len(numbers)==3:
            print(numbers[0])
            exit(0)
        elif numbers[2]==numbers[1] and len(numbers)>3:
            for number in numbers:
                if number!=numbers[0]:
                    print('B')
                    exit(0)
            else:
                print(numbers[0])
                exit(0)
        elif numbers[2]!=numbers[1]:
            print('B')
            exit(0)
    if (numbers[2]-numbers[1])%(numbers[1]-numbers[0]):
        print('B')
        exit(0)
    a=(numbers[2]-numbers[1])//(numbers[1]-numbers[0])
    b=numbers[1]-numbers[0]*a

    ans_candidate=set()

    for i in range(N-1):
        if numbers[i+1]!=numbers[i]*a+b:
            print('B')
            exit(0)
    else:
        print(numbers[-1]*a+b)
        exit(0)