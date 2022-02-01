N=int(input())
initial_value=N

count=0
while True:
    if N<10:
        N=11*N
    else:
        if int(str(N)[0])+int(str(N)[-1])<10:
            N=int(str(N)[-1])*10+int(str(N)[0])+int(str(N)[-1])
        elif int(str(N)[0])+int(str(N)[-1])>=10:
            N=int(str(N)[-1])*10+int(str(N)[0])+int(str(N)[-1])-10
    count=count+1

    if N==initial_value:
        break

print(count)