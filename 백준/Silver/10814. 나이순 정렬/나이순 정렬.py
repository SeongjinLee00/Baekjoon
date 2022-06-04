N=int(input())

words=list()

for _ in range(N):
    s=input()
    words.append(s)

words.sort(key=lambda x:int(x.split()[0]))

for word in words:
    print(word)