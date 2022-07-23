while True:
    try:
        S,N=map(int,input().split())
        
        print(N//(S+1))
    except:
        exit(0)