def solution(a, b, n):
    ans=0
    while True:
        ans+=b*(n//a)
        n=n%a+b*(n//a)
        if n<a:
            return ans