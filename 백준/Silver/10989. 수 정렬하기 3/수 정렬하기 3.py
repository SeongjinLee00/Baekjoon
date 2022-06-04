import sys
input = sys.stdin.readline
N = int(input())

counts = [0]*10001

for _ in range(N):
    counts[int(input())]+=1

for i in range(10001):
    for _ in range(counts[i]):
        print(i)