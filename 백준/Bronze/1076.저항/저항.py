a=input()
b=input()
c=input()

values=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet','grey', 'white']

resistance=0

for s in values:
    if s==a:
        resistance+=10*values.index(s)
    if s==b:
        resistance+=values.index(s)

for s in values:
    if s==c:
        resistance*=10**values.index(s)

print(resistance)