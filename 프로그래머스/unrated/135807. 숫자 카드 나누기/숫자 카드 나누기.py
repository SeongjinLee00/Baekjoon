from math import gcd

def solution(arrayA, arrayB):
    gcdA=arrayA[0]
    
    gcdB=arrayB[0]
    
    arrayA=set(arrayA)
    arrayB=set(arrayB)
    
    for num in arrayA:
        gcdA=gcd(gcdA,num)
    for num in arrayB:
        gcdB=gcd(gcdB,num)
        
    candidates=[0]
    
    divisorsA=[]
    divisorsB=[]
    
    for n in range(1,int(gcdA**0.5)+1):
        if gcdA%n==0:
            divisorsA.append(n)
            divisorsA.append(gcdA//n)
            
    for n in range(1,int(gcdB**0.5)+1):
        if gcdB%n==0:
            divisorsB.append(n)
            divisorsB.append(gcdB//n)

    for divisor in divisorsA:
        for num in arrayB:
            if num%divisor==0:
                break
        else:
            candidates.append(divisor)

    for divisor in divisorsB:
        for num in arrayA:
            if num%divisor==0:
                break
        else:
            candidates.append(divisor)

    return max(candidates)