from collections import Counter

def solution(spell, dic):
    for word in dic:
        if Counter(word)==Counter(spell):
            return 1
    
    return 2