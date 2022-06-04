N=int(input())
numbers=list(map(int,input().split()))
numbers_set=set(numbers)

sorted_list=sorted(list(numbers_set))
numbers_dict={}

N=len(sorted_list)-1

while N>=0:
    numbers_dict[sorted_list.pop()]=N
    N-=1

for number in numbers:
    print(numbers_dict[number], end=' ')