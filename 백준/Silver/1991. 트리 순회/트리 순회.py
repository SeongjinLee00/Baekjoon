tree=dict()
N=int(input())
for i in range(1,N+1):
    a,b,c=input().split()
    tree[a]=[b,c]

def preorder(T):
    if T!='.':
        print(T,end='')
        preorder(tree[T][0])
        preorder(tree[T][1])

def inorder(T):
    if T!='.':
        inorder(tree[T][0])
        print(T,end='')
        inorder(tree[T][1])

def postorder(T):
    if T!='.':
        postorder(tree[T][0])
        postorder(tree[T][1])
        print(T,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')