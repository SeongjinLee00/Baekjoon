S=input()
for c in S:
    if c.isupper():
        print(c.lower(),end='')
    else:
        print(c.upper(),end='')