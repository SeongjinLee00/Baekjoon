N=int(input())

list1=[]

count=0
for i in range(N):
    if i+sum([int(i) for i in str(i)])==N:
        print(i)
        count=count+1
        break

if count==0:
    print(0)