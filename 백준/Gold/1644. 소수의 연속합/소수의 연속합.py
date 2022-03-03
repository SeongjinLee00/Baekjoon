N=int(input())

if N==1:
    print(0)
elif N==2:
    print(1)
elif N==3:
    print(1)
elif N==4:
    print(0)
else:
    a = [False,False] + [True]*(N-1)
    primes=[]
    for i in range(2,N+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, N+1, i):
                a[j] = False

    i=0
    j=1
    partialsum=primes[i]+primes[j]
    length=len(primes)
    cnt=0

    while j<length:
        if partialsum==N:
            try:
                cnt+=1
                j+=1
                partialsum+=primes[j]
                partialsum-=primes[i]
                i+=1
            except:
                break
        elif partialsum<N:
            try:
                j+=1
                partialsum+=primes[j]
            except:
                break
        elif partialsum>N:
            partialsum-=primes[i]
            i+=1

    print(cnt)