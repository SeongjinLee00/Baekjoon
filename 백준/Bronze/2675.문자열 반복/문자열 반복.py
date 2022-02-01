T=int(input())

for _ in range(T):
    num, word=input().split()
    num=int(num)

    for i in range(len(word)):
        print(word[i]*num,end='')
    print('')