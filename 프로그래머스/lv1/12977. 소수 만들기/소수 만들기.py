primes=[0,0]+[1]*3000

for i in range(2,56):
    for j in range(2*i,3002,i):
        primes[j]=0

def solution(nums):
    ans=0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                if primes[nums[i]+nums[j]+nums[k]]:
                    ans+=1
    
    return ans