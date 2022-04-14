N=int(input())

numbers=list(map(int,input().split()))

numbers.sort()

minvalue=9999999999999

ans=[]
for k in range(N-2):
    i=k+1
    j=N-1
    
    while i<j:
        partialsum=numbers[k]+numbers[i]+numbers[j]
        if abs(partialsum)<minvalue:
            ans=[numbers[k],numbers[i],numbers[j]]
            minvalue=abs(partialsum)

        if partialsum<0:
            i+=1
        elif partialsum>0:
            j-=1
        elif partialsum==0:
            print(numbers[k],numbers[i],numbers[j])
            exit(0)

print(*ans)