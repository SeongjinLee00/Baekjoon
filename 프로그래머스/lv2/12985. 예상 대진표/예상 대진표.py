def solution(n,a,b):
    answer = 1

    while True:
        if abs(a-b)==1 and ((a<b and a%2) or (b<a and b%2)):
            return answer
        else:
            a=(a+1)//2
            b=(b+1)//2
            answer+=1