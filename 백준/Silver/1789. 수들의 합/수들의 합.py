ans=1

S=int(input())

while True:
    if ans*(ans+1)//2>S:
        print(ans-1)
        exit(0)
    
    ans+=1