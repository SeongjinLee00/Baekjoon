def solution(brown, yellow):

    for sero in range(1,2000):
        for garo in range(sero,2000):
            if garo*2+sero*2-4==brown and garo*sero==brown+yellow:
                return [garo,sero]