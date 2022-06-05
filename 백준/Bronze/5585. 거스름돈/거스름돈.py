n=int(input())
target=1000-n
ans=0
ans+=target//500
target-=(target//500)*500
ans+=target//100
target-=(target//100)*100
ans+=target//50
target-=(target//50)*50
ans+=target//10
target-=(target//10)*10
ans+=target//5
target-=(target//5)*5
ans+=target//1
target-=(target//1)*1

print(ans)