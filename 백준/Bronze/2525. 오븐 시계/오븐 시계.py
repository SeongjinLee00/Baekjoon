A,B=map(int,input().split())
C=int(input())

minute=(B+C)%60
dh=(B+C)//60

hour=(A+dh)%24

print(hour,minute)