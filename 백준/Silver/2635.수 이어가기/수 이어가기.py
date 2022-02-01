N=int(input())

numbers1=[]
numbers2=[]

front=0
back=0

for i in range(1,N+1):
    numbers1=[]
    front=N
    back=i
    numbers1.append(front)
    numbers1.append(back)
    while back>=0:
        front,back=back,front-back
        numbers1.append(back)

    if len(numbers2)<len(numbers1):
        numbers2=numbers1
numbers2.pop()
print(len(numbers2))
for number in numbers2:
    print(number,end=' ')