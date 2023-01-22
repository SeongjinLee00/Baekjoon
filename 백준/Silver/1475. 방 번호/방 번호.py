from collections import Counter
from math import ceil

d=Counter(input())

print(max(d['0'],d['1'],d['2'],d['3'],d['4'],d['5'],d['7'],d['8'],ceil((d['6']+d['9'])/2)))