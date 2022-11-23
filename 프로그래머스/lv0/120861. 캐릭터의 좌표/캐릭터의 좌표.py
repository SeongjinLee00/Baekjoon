def solution(keyinput, board):
    mx,my=board[0]//2, board[1]//2
    
    x=0
    y=0
    for item in keyinput:
        if item=='left':
            x-=1
            if x<-mx:
                x+=1
        elif item=='right':
            x+=1
            if x>mx:
                x-=1
        elif item=='up':
            y+=1
            if y>my:
                y-=1
        elif item=='down':
            y-=1
            if y<-my:
                y+=1
    return [x,y]