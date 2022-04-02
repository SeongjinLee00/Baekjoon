def rotate(command):
    face=command[0]
    dir=command[1]

    if face=='U':
        if dir=='+':
            cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['up'][0][1],cube['up'][1][1],cube['up'][2][1],cube['up'][0][0],cube['up'][1][0],cube['up'][2][0]=cube['up'][0][0],cube['up'][0][1],cube['up'][0][2],cube['up'][1][0],cube['up'][1][1],cube['up'][1][2],cube['up'][2][0],cube['up'][2][1],cube['up'][2][2]

        elif dir=='-':
            cube['up'][0][0],cube['up'][0][1],cube['up'][0][2],cube['up'][1][0],cube['up'][1][1],cube['up'][1][2],cube['up'][2][0],cube['up'][2][1],cube['up'][2][2]=cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['up'][0][1],cube['up'][1][1],cube['up'][2][1],cube['up'][0][0],cube['up'][1][0],cube['up'][2][0]

    elif face=='D':
        if dir=='+':
            cube['down'][0][2],cube['down'][1][2],cube['down'][2][2],cube['down'][0][1],cube['down'][1][1],cube['down'][2][1],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0]=cube['down'][0][0],cube['down'][0][1],cube['down'][0][2],cube['down'][1][0],cube['down'][1][1],cube['down'][1][2],cube['down'][2][0],cube['down'][2][1],cube['down'][2][2]

        elif dir=='-':
            cube['down'][0][0],cube['down'][0][1],cube['down'][0][2],cube['down'][1][0],cube['down'][1][1],cube['down'][1][2],cube['down'][2][0],cube['down'][2][1],cube['down'][2][2]=cube['down'][0][2],cube['down'][1][2],cube['down'][2][2],cube['down'][0][1],cube['down'][1][1],cube['down'][2][1],cube['down'][0][0],cube['down'][1][0],cube['down'][2][0]

    elif face=='F':
        if dir=='+':
            cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['front'][0][1],cube['front'][1][1],cube['front'][2][1],cube['front'][0][0],cube['front'][1][0],cube['front'][2][0]=cube['front'][0][0],cube['front'][0][1],cube['front'][0][2],cube['front'][1][0],cube['front'][1][1],cube['front'][1][2],cube['front'][2][0],cube['front'][2][1],cube['front'][2][2]

        elif dir=='-':
            cube['front'][0][0],cube['front'][0][1],cube['front'][0][2],cube['front'][1][0],cube['front'][1][1],cube['front'][1][2],cube['front'][2][0],cube['front'][2][1],cube['front'][2][2]=cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['front'][0][1],cube['front'][1][1],cube['front'][2][1],cube['front'][0][0],cube['front'][1][0],cube['front'][2][0]

    elif face=='B':
        if dir=='+':
            cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['back'][0][1],cube['back'][1][1],cube['back'][2][1],cube['back'][0][0],cube['back'][1][0],cube['back'][2][0]=cube['back'][0][0],cube['back'][0][1],cube['back'][0][2],cube['back'][1][0],cube['back'][1][1],cube['back'][1][2],cube['back'][2][0],cube['back'][2][1],cube['back'][2][2]

        elif dir=='-':
            cube['back'][0][0],cube['back'][0][1],cube['back'][0][2],cube['back'][1][0],cube['back'][1][1],cube['back'][1][2],cube['back'][2][0],cube['back'][2][1],cube['back'][2][2]=cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['back'][0][1],cube['back'][1][1],cube['back'][2][1],cube['back'][0][0],cube['back'][1][0],cube['back'][2][0]

    elif face=='L':
        if dir=='+':
            cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['left'][0][1],cube['left'][1][1],cube['left'][2][1],cube['left'][0][0],cube['left'][1][0],cube['left'][2][0]=cube['left'][0][0],cube['left'][0][1],cube['left'][0][2],cube['left'][1][0],cube['left'][1][1],cube['left'][1][2],cube['left'][2][0],cube['left'][2][1],cube['left'][2][2]

        elif dir=='-':
            cube['left'][0][0],cube['left'][0][1],cube['left'][0][2],cube['left'][1][0],cube['left'][1][1],cube['left'][1][2],cube['left'][2][0],cube['left'][2][1],cube['left'][2][2]=cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['left'][0][1],cube['left'][1][1],cube['left'][2][1],cube['left'][0][0],cube['left'][1][0],cube['left'][2][0]

    elif face=='R':
        if dir=='+':
            cube['right'][0][2],cube['right'][1][2],cube['right'][2][2],cube['right'][0][1],cube['right'][1][1],cube['right'][2][1],cube['right'][0][0],cube['right'][1][0],cube['right'][2][0]=cube['right'][0][0],cube['right'][0][1],cube['right'][0][2],cube['right'][1][0],cube['right'][1][1],cube['right'][1][2],cube['right'][2][0],cube['right'][2][1],cube['right'][2][2]

        elif dir=='-':
            cube['right'][0][0],cube['right'][0][1],cube['right'][0][2],cube['right'][1][0],cube['right'][1][1],cube['right'][1][2],cube['right'][2][0],cube['right'][2][1],cube['right'][2][2]=cube['right'][0][2],cube['right'][1][2],cube['right'][2][2],cube['right'][0][1],cube['right'][1][1],cube['right'][2][1],cube['right'][0][0],cube['right'][1][0],cube['right'][2][0]

def translate(command):
    face=command[0]
    dir=command[1]

    if face=='U':
        if dir=='+':
            cube['front'][0],cube['right'][0],cube['back'][0],cube['left'][0]=cube['right'][0],cube['back'][0],cube['left'][0],cube['front'][0]
        elif dir=='-':
            cube['right'][0],cube['back'][0],cube['left'][0],cube['front'][0]=cube['front'][0],cube['right'][0],cube['back'][0],cube['left'][0]

    elif face=='D':
        if dir=='-':
            cube['front'][2],cube['right'][2],cube['back'][2],cube['left'][2]=cube['right'][2],cube['back'][2],cube['left'][2],cube['front'][2]
        elif dir=='+':
            cube['right'][2],cube['back'][2],cube['left'][2],cube['front'][2]=cube['front'][2],cube['right'][2],cube['back'][2],cube['left'][2]

    elif face=='F':
        if dir=='+':
            cube['right'][2][0],cube['right'][1][0],cube['right'][0][0],cube['up'][2][2],cube['up'][2][1],cube['up'][2][0],cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['down'][0][0],cube['down'][0][1],cube['down'][0][2]=cube['up'][2][2],cube['up'][2][1],cube['up'][2][0],cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['down'][0][0],cube['down'][0][1],cube['down'][0][2],cube['right'][2][0],cube['right'][1][0],cube['right'][0][0]
        elif dir=='-':
            cube['up'][2][2],cube['up'][2][1],cube['up'][2][0],cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['down'][0][0],cube['down'][0][1],cube['down'][0][2],cube['right'][2][0],cube['right'][1][0],cube['right'][0][0]=cube['right'][2][0],cube['right'][1][0],cube['right'][0][0],cube['up'][2][2],cube['up'][2][1],cube['up'][2][0],cube['left'][0][2],cube['left'][1][2],cube['left'][2][2],cube['down'][0][0],cube['down'][0][1],cube['down'][0][2]

    elif face=='R':
        if dir=='+':
            cube['back'][2][0],cube['back'][1][0],cube['back'][0][0],cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['down'][0][2],cube['down'][1][2],cube['down'][2][2]=cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['down'][0][2],cube['down'][1][2],cube['down'][2][2],cube['back'][2][0],cube['back'][1][0],cube['back'][0][0]
        elif dir=='-':
            cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['down'][0][2],cube['down'][1][2],cube['down'][2][2],cube['back'][2][0],cube['back'][1][0],cube['back'][0][0]=cube['back'][2][0],cube['back'][1][0],cube['back'][0][0],cube['up'][0][2],cube['up'][1][2],cube['up'][2][2],cube['front'][0][2],cube['front'][1][2],cube['front'][2][2],cube['down'][0][2],cube['down'][1][2],cube['down'][2][2]

    elif face=='L':
        if dir=='+':
            cube['front'][2][0],cube['front'][1][0],cube['front'][0][0],cube['up'][2][0],cube['up'][1][0],cube['up'][0][0],cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['down'][2][0],cube['down'][1][0],cube['down'][0][0]=cube['up'][2][0],cube['up'][1][0],cube['up'][0][0],cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['down'][2][0],cube['down'][1][0],cube['down'][0][0],cube['front'][2][0],cube['front'][1][0],cube['front'][0][0]
        elif dir=='-':
            cube['up'][2][0],cube['up'][1][0],cube['up'][0][0],cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['down'][2][0],cube['down'][1][0],cube['down'][0][0],cube['front'][2][0],cube['front'][1][0],cube['front'][0][0]=cube['front'][2][0],cube['front'][1][0],cube['front'][0][0],cube['up'][2][0],cube['up'][1][0],cube['up'][0][0],cube['back'][0][2],cube['back'][1][2],cube['back'][2][2],cube['down'][2][0],cube['down'][1][0],cube['down'][0][0]

    elif face=='B':
        if dir=='-':
            cube['left'][0][0],cube['left'][1][0],cube['left'][2][0],cube['down'][2][0],cube['down'][2][1],cube['down'][2][2],cube['right'][2][2],cube['right'][1][2],cube['right'][0][2],cube['up'][0][2],cube['up'][0][1],cube['up'][0][0]=cube['down'][2][0],cube['down'][2][1],cube['down'][2][2],cube['right'][2][2],cube['right'][1][2],cube['right'][0][2],cube['up'][0][2],cube['up'][0][1],cube['up'][0][0],cube['left'][0][0],cube['left'][1][0],cube['left'][2][0]
        elif dir=='+':
            cube['down'][2][0],cube['down'][2][1],cube['down'][2][2],cube['right'][2][2],cube['right'][1][2],cube['right'][0][2],cube['up'][0][2],cube['up'][0][1],cube['up'][0][0],cube['left'][0][0],cube['left'][1][0],cube['left'][2][0]=cube['left'][0][0],cube['left'][1][0],cube['left'][2][0],cube['down'][2][0],cube['down'][2][1],cube['down'][2][2],cube['right'][2][2],cube['right'][1][2],cube['right'][0][2],cube['up'][0][2],cube['up'][0][1],cube['up'][0][0]

T=int(input())
for _ in range(T):
    N=int(input())
    commands=list(input().split())
    cube={
    'up':[['w','w','w'],
        ['w','w','w'],
        ['w','w','w']],
    'down':[['y','y','y'],
        ['y','y','y'],
        ['y','y','y']],
    'front':[['r','r','r'],
        ['r','r','r'],
        ['r','r','r']],
    'back':[['o','o','o'],
        ['o','o','o'],
        ['o','o','o']],
    'left':[['g','g','g'],
        ['g','g','g'],
        ['g','g','g']],
    'right':[['b','b','b'],
        ['b','b','b'],
        ['b','b','b']],
    }
    for command in commands:
        translate(command)
        rotate(command)
    for row in cube['up']:
        print(''.join(row))