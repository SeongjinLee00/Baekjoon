from itertools import product

n,m=map(int,input().split())

formulae=[]

for _ in range(m):
    formulae.append(list(map(int,input().split())))

for item in product([-1,1],repeat=n):
    for formula in formulae:
        if (formula[0]*item[abs(formula[0])-1])*(formula[1]*item[abs(formula[1])-1])>0 and (formula[0]*item[abs(formula[0])-1])+(formula[1]*item[abs(formula[1])-1])<0:
            break
    else:
        print(1)
        for i in range(n):
            print(int(item[i]*0.5+0.5),end=' ')
        exit(0)

print(0)