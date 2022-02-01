N=int(input())

five=N//5
three=(N-five*5)//3

if N==3:
    print(1)
elif N==4:
    print(-1)
elif N%5==0:
    print(five)
elif N%5==1:
    five=five-1
    three=three+2
    print(five+three)
elif N==7:
    print(-1)
elif N%5==2:
    five=five-2
    three=three+4
    print(five+three)
elif N%5==3:
    print(five+three)
elif N%5==4:
    five=five-1
    three=three+2
    print(five+three)