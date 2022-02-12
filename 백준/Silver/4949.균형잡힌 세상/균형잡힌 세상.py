while True:
    s = input()
    if s == '.':
        break

    stack=['X']
    indicator=0
    for d in s:
        if d=='(':
            stack.append(d)
        if d==')':
            if stack[-1]!='(':
                indicator+=1
                break
            else:
                stack.pop()
        if d=='[':
            stack.append(d)
        if d==']':
            if stack[-1]!='[':
                indicator+=1
                break
            else:
                stack.pop()
    if indicator!=0 or stack[-1]!='X':
        print('no')
    else:
        print('yes')