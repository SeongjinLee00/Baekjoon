N=int(input())

words=[set() for _ in range(51)]

for _ in range(N):
    s=input()
    words[len(s)].add(s)

for item in words:
    if item:
        arr=list(item)
        arr.sort()
        for word in arr:
            print(word)