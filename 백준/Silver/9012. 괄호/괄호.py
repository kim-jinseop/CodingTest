t = int(input())

for _ in range(t) :
    text = input()
    stack = []
    for i in text :
        if i == '(' :
            stack.append(i)
        else :
            if stack :
                stack.pop()
            else :
                print('NO')
                break
    else :
        if stack :
            print("NO")
        else :
            print("YES")