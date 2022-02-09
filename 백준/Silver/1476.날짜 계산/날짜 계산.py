a1,a2,a3=map(int,input().split())

m1,m2,m3=15,28,19

n1=m2*m3
n2=m1*m3
n3=m1*m2

s1=1
s2=1
s3=1
for _ in range(1,n1+1):
    if (s1*n1)%m1==1:
        break
    else:
        s1=s1+1

for _ in range(1,n2+1):
    if (s2*n2)%m2==1:
        break
    else:
        s2=s2+1

for _ in range(1,n3+1):
    if (s3*n3)%m3==1:
        break
    else:
        s3=s3+1

X=a1*n1*s1+a2*n2*s2+a3*n3*s3
M=m1*m2*m3
while X>M:
    X=X-M

print(X)