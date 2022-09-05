def solution(s):

    for c in s:
        if not c.isnumeric():
            return False
    if len(s)==4 or len(s)==6:
        return True
    return False