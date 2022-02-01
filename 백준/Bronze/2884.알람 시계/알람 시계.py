hour,min=map(int,input().split())

if min>=45:
    min=min-45
    print(f'{hour} {min}')

elif hour==0 and min<45:
    hour=23
    min=min+15
    print(f'{hour} {min}')

elif min<45:
    hour=hour-1
    min=min+15
    print(f'{hour} {min}')