K=int(input())
n=int(input())

dp=[0,set(),set(),set(),set(),set(),set(),set(),set()]

dp[1].add(K)
dp[2].add(11*K)
dp[3].add(111*K)
dp[4].add(1111*K)
dp[5].add(11111*K)
dp[6].add(111111*K)
dp[7].add(1111111*K)
dp[8].add(11111111*K)

for i in range(1,9):
    for j in range(1,i+1):
        kind=i+j
        if kind>8:
            continue
        
        for num1 in dp[i]:
            for num2 in dp[j]:
                dp[kind].add(num1+num2)
                if num1!=num2:
                    dp[kind].add(abs(num1-num2))
                dp[kind].add(num1*num2)

                if num1>num2:
                    dp[kind].add(num1//num2)
                else:
                    dp[kind].add(num2//num1)


for _ in range(n):
    a=int(input())
    res=-1

    for i in range(1,9):
        if a in dp[i]:
            res=i
            break
    
    if res==-1:
        print('NO')
    else:
        print(res)