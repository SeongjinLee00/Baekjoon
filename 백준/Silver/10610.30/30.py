N=input()

if ('0' not in N) or sum(map(int,list(N)))%3!=0:
    print(-1)
else:
    N_list=list(N)
    N_list.sort(reverse=True)
    N_str=''.join(N_list)

    print(N_str)