K=int(input())

money=[]

for _ in range(K):
    a=int(input())

    if a==0:
        money.pop()
    else:
        money.append(a)

print(sum(money))