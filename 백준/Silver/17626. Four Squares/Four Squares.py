import math

li1=[]
li2=[]
li3=[]

for i in range(1,int(math.sqrt(50001))+1):
    li1.append(i*i)

for i in range(len(li1)):
    for j in range(i,len(li1)):
        li2.append(li1[i]+li1[j])

for i in range(len(li1)):
    for j in range(i,len(li1)):
        for k in range(j,len(li1)):
            li3.append(li1[i]+li1[j]+li1[k])

N=int(input())

if N in li1:
    print(1)
elif N in li2:
    print(2)
elif N in li3:
    print(3)
else:
    print(4)