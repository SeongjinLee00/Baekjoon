from itertools import permutations

N=int(input())
numbers=list(map(int,input().split()))
operators_number=list(map(int,input().split()))

operators=['+']*operators_number[0]+['-']*operators_number[1]+['*']*operators_number[2]+['/']*operators_number[3]

permutation=permutations(operators,N-1)

ans_max=-float('inf')
ans_min=float('inf')
for order in permutation:
    tmp=numbers[0]
    for i in range(len(order)):
        if order[i]=='+':
            tmp+=numbers[i+1]
        elif order[i]=='-':
            tmp-=numbers[i+1]
        elif order[i]=='*':
            tmp*=numbers[i+1]
        elif order[i]=='/':
            if tmp>0:
                tmp=tmp//numbers[i+1]
            elif tmp<0:
                tmp=-tmp
                tmp=tmp//numbers[i+1]
                tmp=-tmp
            else:
                tmp=0
    
    if tmp>ans_max:
        ans_max=tmp
    if tmp<ans_min:
        ans_min=tmp

print(ans_max)
print(ans_min)