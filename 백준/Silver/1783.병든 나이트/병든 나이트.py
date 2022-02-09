N,M=map(int,input().split())

if N==1 or M==1:
    print(1)

elif N<=2 and M<=2:
    print(1)

elif N==2:
    if ((M-1)//2+1)<4:
        print((M-1)//2+1)
    else:
        print(4)

elif M==2:
    print(2)

elif M<7:
    if M<4:
        print(M)
    else:
        print(4)

else:
    print(M-2)