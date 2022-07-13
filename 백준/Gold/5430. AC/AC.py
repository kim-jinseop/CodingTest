from sys import stdin
from collections import deque

t = int(stdin.readline())

for _ in range(t) :
    rd = stdin.readline().rstrip()
    n = int(stdin.readline())
    arr = stdin.readline().rstrip()
    arr = arr[1:len(arr)-1].split(',')
    q = deque(arr)
    reverse = 0

    for i in rd :
        if i == 'R' :
            if reverse : reverse = 0
            else : reverse = 1

        elif i == 'D' :
            if q :
                if reverse : q.pop()
                else : q.popleft()
            n -= 1
    
    if n < 0 :
        print('error')
    else :
        if reverse : q.reverse()

        print('[',end='')
        print(','.join(q),end='')
        print(']')