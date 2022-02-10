def gcd(num1,num2): # Euclidian 
    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    r=a%b
    if a%b==0:
        return b
    else:
        return gcd(b,r)
def lcm(num1,num2):
    return num1*num2//gcd(num1,num2)
#####################################################################################
#####################################################################################
N=int(input())

numbers=[]
for _ in range(N):
    numbers.append(int(input()))

numbers.sort(reverse=True)
minus=[]
for i in range(len(numbers)-1):
    minus.append(numbers[i]-numbers[i+1])

if N==2:
    allgcd=minus[0]
else:
    allgcd=gcd(minus[0],minus[1])

for i in range(len(minus)):
    allgcd=gcd(allgcd,minus[i])

for i in range(2, allgcd+1):
    if allgcd%i==0:
        print(i,end=' ')