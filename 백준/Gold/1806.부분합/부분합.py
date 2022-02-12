N,S=map(int,input().split())

numbers=list(map(int,input().split()))

if max(numbers)>=S:
    print(1)
else:
    i=0
    j=1
    partialsum=numbers[i]+numbers[j]
    minlength=9999999
    while j<N:
        if partialsum<S:
            try:
                j+=1
                partialsum+=numbers[j]
            except:
                break
        if partialsum>=S:
            if j-i+1<minlength:
                minlength=j-i+1
            partialsum-=numbers[i]
            i+=1

    if minlength==9999999:
        print(0)
    else:
        print(minlength)