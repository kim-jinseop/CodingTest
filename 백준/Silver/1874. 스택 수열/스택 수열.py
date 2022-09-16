from sys import stdin

n = int(stdin.readline())
arr = list(range(1,n+1))
stack = []
result = []
chk = 0

for i in range(n) :
    tgt = int(stdin.readline())

    while arr :
        if not stack :
            stack.append(arr.pop(0))
            result.append('+')

        elif stack[-1] == tgt :
            stack.pop()
            result.append('-')
            break

        else :
            stack.append(arr.pop(0))
            result.append('+')

    else :
        if stack[-1] == tgt :
            stack.pop()
            result.append('-')
        else :
            chk = 1
            break

if chk :
    print('NO')
else :
    for i in result :
        print(i)