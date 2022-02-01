T=int(input())

for _ in range(T):
    a, *card_a=map(int,input().split())
    b, *card_b=map(int,input().split())

    if card_a.count(4)==card_b.count(4):
        if card_a.count(3)==card_b.count(3):
            if card_a.count(2)==card_b.count(2):
                if card_a.count(1)==card_b.count(1):
                    print('D')

                else:
                    if card_a.count(1)>card_b.count(1):
                        print('A')
                    else:
                        print('B')
            else:
                if card_a.count(2)>card_b.count(2):
                    print('A')
                else:
                    print('B')
        else:
            if card_a.count(3)>card_b.count(3):
                print('A')
            else:
                print('B')
    else:
        if card_a.count(4)>card_b.count(4):
            print('A')
        else:
            print('B')