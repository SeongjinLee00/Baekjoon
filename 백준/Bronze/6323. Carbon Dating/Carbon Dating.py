from math import log2

t=1
while True:
    w,d=map(int,input().split())

    if w==0 and d==0:
        exit(0)
    
    tau=log2(810)-log2(d/w)

    years=5730*tau

    if years<10000:
        years=int(round(years,-2))
    else:
        years=int(round(years,-3))

    print(f"Sample #{t}")
    print(f"The approximate age is {years} years.")
    print()
    t+=1