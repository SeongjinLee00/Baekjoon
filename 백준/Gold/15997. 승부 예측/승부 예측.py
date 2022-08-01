from itertools import product

a,b,c,d=input().split()

cases=product([0,1,2],repeat=6)

scores=[{'case':i,'probability':1, a:0,b:0,c:0,d:0} for i in range(729)]

odds=[]

for _ in range(6):
    odds.append(list(input().split()))

cnt=0
for case in cases:
    for i in range(len(case)):
        if case[i]==0:
            scores[cnt]['probability']*=float(odds[i][2])
            scores[cnt][odds[i][0]]+=3
        elif case[i]==1:
            scores[cnt]['probability']*=float(odds[i][3])
            scores[cnt][odds[i][0]]+=1
            scores[cnt][odds[i][1]]+=1
        elif case[i]==2:
            scores[cnt]['probability']*=float(odds[i][4])
            scores[cnt][odds[i][1]]+=3
    cnt+=1

def second_largest_number(arr):
    second = largest = -float('inf') 
    
    for n in arr:
        if n > largest:
            second = largest
            largest = n
        elif second < n < largest:
            second = n

    return second

ans=[0,0,0,0]
for item in scores:
    l=[item[a],item[b],item[c],item[d]]
    tmp=[]
    ml=max(l)
    for i in range(4):
        if l[i]==ml:
            tmp.append(i)
    lt=len(tmp)
    for ii in tmp:
        if lt==1: ans[ii]+=item['probability']/(lt)
        elif lt>=2: ans[ii]+=(2*item['probability']/(lt))
    if lt==1:
        tmp2=[]
        sl=second_largest_number(l)
        for j in range(4):
            if j==tmp[0]:
                continue
            if l[j]==sl:
                tmp2.append(j)
        for jj in tmp2:
            ans[jj]+=item['probability']/(len(tmp2))

for item in ans:
    print(item)