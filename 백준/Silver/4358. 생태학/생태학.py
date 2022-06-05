from collections import defaultdict

import sys

di=defaultdict(int)
se=set()
cnt=0
while True:

    name=sys.stdin.readline().rstrip()
    if not name:
        break
    di[name]+=1
    se.add(name)

    cnt+=1

se=sorted(list(se))

for name in se:
    print(f'{name} {di[name]/cnt*100:.4f}')