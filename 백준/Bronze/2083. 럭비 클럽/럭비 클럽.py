while True:
    s,a,b=input().split()
    if s=='#':
        exit(0)
    
    if int(a)>17 or int(b)>=80:
        print(f'{s} Senior')
    else:
        print(f'{s} Junior')