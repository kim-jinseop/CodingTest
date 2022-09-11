from sys import stdin
from collections import deque

n = int(stdin.readline())
q = deque()

for _ in range(n) :
    x = stdin.readline().split()
    
    if x[0] == 'push' :
        q.append(x[1])
    elif x[0] == 'pop' :
        if q :
            print(q.popleft())
        else :
            print(-1)
    elif x[0] == 'size' :
        print(len(q))
    elif x[0] == 'empty' :
        if q :
            print(0)
        else :
            print(1)
    elif x[0] == 'front' :
        if q :
            print(q[0])
        else :
            print(-1)
    elif x[0] == 'back' :
        if q :
            print(q[-1])
        else :
            print(-1)