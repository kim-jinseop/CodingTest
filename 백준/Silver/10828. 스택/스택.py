from sys import stdin

n = int(stdin.readline())
stack = []

for _ in range(n) :
    box = stdin.readline().split()

    if box[0] == 'push' :
        stack.append(int(box[1]))
    elif box[0] == 'pop' :
        if stack :
            print(stack.pop())
        else :
            print(-1)
    elif box[0] == 'top' :
        if stack :
            print(stack[-1])
        else :
            print(-1)
    elif box[0] == 'empty' :
        if stack :
            print(0)
        else :
            print(1)
    elif box[0] == 'size' :
        print(len(stack))