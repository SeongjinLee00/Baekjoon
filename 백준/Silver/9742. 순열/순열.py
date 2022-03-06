def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(my_str,l):
    global cnt
    if l==len(s):
        cnt+=1
        if cnt==n:
            return my_str

    else:
        for c in s:
            if c not in my_str:
                r=permutation(my_str+c,l+1)
                if r:
                    return r
                
while True:
    try:
        s,n=input().split()
        cnt=0
        n=int(n)
        if n>factorial(len(s)):
            print(s,n,'=','No permutation')
        else:
            print(s,n,'=',permutation('',0))
    except:
        exit(0)