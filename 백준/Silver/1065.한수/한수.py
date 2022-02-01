N=int(input())

def is_hansu(num):
    if num<10:
        return True
    elif num<100:
        return True
    elif num<1000:
        if int(str(num)[0])+int(str(num)[2])==2*int(str(num)[1]):
            return True
        else:
            return False

count=0

for i in range(1,N+1):
    if is_hansu(i)==True:
        count=count+1

print(count)