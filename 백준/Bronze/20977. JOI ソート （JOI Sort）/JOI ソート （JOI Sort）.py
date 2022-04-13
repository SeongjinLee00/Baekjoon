N=int(input())
s=input()
a=s.count('J')
b=s.count('O')
c=s.count('I')
for _ in range(a):
    print('J',end='')
for _ in range(b):
    print('O',end='')
for _ in range(c):
    print('I',end='')