n=int(input())
my=int(input())

if my<=n:
    print('Congratulations, you are within the speed limit!')
elif n+1<=my<=n+20:
    print('You are speeding and your fine is $100.')
elif n+21<=my<=n+30:
    print('You are speeding and your fine is $270.')
elif n+31<=my:
    print('You are speeding and your fine is $500.')