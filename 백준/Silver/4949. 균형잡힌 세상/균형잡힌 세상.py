from sys import stdin

text = stdin.read().split('\n')

for t in text :
    stack = []

    if t == '.' :
        break

    for i in t :
        if i == '(' or i=='[' :
            stack.append(i)

        elif i == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                print('no')
                break

        elif i == ']' :
            if stack and stack[-1] == '[' :
                stack.pop()
            else :
                print('no')
                break

        elif i == '.' :
            if stack :
                print('no')
            else :
                print('yes')