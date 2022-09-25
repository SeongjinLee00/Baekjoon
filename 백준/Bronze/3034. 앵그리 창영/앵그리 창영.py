n,w,h=map(int,input().split())
d=((w*w+h*h)**0.5)

for _ in range(n):
    if int(input())>d:
        print('NE')
    else:
        print('DA')