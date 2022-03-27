from itertools import combinations

l,c=map(int,input().split())

alphabet=list(input().split())

alphabet.sort()

comb=combinations(alphabet,l)

for item in comb:
    vowel=item.count('a')+item.count('e')+item.count('i')+item.count('o')+item.count('u')
    if vowel>=1 and len(item)-vowel>=2:
        print(''.join(item))