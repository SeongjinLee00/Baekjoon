def solution(s):
    p=s.count('p')+s.count('P')
    y=s.count('y')+s.count('Y')
    if p+y==0:
        return True
    return p==y