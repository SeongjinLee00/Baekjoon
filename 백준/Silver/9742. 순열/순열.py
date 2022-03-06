def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

def permutation(my_str,l):
    global cnt
    global ans

    if l==len(s):
        cnt+=1
        if cnt==n:
            ans=my_str

    else:
        for c in s:
            if c not in my_str:
                permutation(my_str+c,l+1)
                if ans:
                    return

while True:
    try:
        s,n=input().split()
        cnt=0
        ans=''
        n=int(n)
        if n>factorial(len(s)):
            print(s,n,'=','No permutation')
        else:
            permutation('',0)
            print(s,n,'=',ans)
    except:
        exit(0)