import sys
sys.setrecursionlimit(10**6)
numbers=[]

while True:
    try:
        n=int(sys.stdin.readline())
        numbers.append(n)
    except:
        break

def subtree(arr):
    if len(arr)==1:
        print(arr[0])
        return
    if len(arr)==0:
        return

    root=arr[0]
    mid=len(arr)
    for i in range(1,len(arr)):
        if arr[i]>root:
            mid=i
            break

    subtree(arr[1:mid])
    subtree(arr[mid:])
    print(root)

subtree(numbers)