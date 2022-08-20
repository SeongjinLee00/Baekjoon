arr=[]

A,B=map(int,input().split())

for number in range(1,50):
    for _ in range(number):
        arr.append(number)

print(sum(arr[A-1:B]))