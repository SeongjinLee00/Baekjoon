from collections import deque

def solution(cacheSize, cities):
    if cacheSize==0:
        return 5*len(cities)
    for i in range(len(cities)):
        cities[i]=cities[i].lower()

    cache=deque()
    
    ans=0
    
    for city in cities:
        if len(cache)<cacheSize:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                ans+=1
            else:
                cache.append(city)
                ans+=5
        else:
            if city in cache:
                cache.remove(city)
                cache.append(city)
                ans+=1
            else:
                cache.popleft()
                cache.append(city)
                ans+=5
    return ans