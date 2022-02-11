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
string=input()

num1=''
num2=''
for s in string:
    if s!=':':
        num1 += s
    else:
        break

for s in string[::-1]:
    if s!=':':
        num2 += s
    else:
        break
num2=num2[::-1]

num1=int(num1)
num2=int(num2)
d=gcd(num1,num2)
num1=num1//d
num2=num2//d

print(f'{num1}:{num2}')