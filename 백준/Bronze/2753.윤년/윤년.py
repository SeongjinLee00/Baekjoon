year=int(input())

dbssus=0

if year%4==0 and year%100!=0:
    dbssus=1

if year%400==0:
    dbssus=1

print(dbssus)