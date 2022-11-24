from collections import Counter

def solution(X, Y):
    candidates=[]
    
    X=Counter(X)
    Y=Counter(Y)
    
    for c in X:
        if c in Y:
            for _ in range(min(X[c],Y[c])):
                candidates.append(c)
            
    if not candidates:
        return '-1'
    elif max(candidates)=='0':
        return '0'
    else:
        return "".join(sorted(candidates,reverse=True))