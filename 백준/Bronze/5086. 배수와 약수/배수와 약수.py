while True:
    a,b=map(int,input().split())

    if a==0 and b==0:
        exit(0)

    if not a%b:
        print('multiple')
    elif not b%a:
        print('factor')
    else:
        print('neither')