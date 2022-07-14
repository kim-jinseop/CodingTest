from sys import stdin
from collections import deque

n,m,x,y,k = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]
step = list(map(int,stdin.readline().split()))

dice_up = [0,0,0] # 위 [1] 아래 [1]
dice_down = [0,0,0]

dx = [0,1,-1,0,0]
dy = [0,0,0,-1,1]

def dice_move(step) :
    if step == 1:
        down = dice_down.pop(1)
        up = dice_up.pop(2)
        dice_up.insert(0,down)
        dice_down.insert(1,up)
    elif step == 2:
        down = dice_down.pop(1)
        up = dice_up.pop(0)
        dice_up.append(down)
        dice_down.insert(1,up)
    elif step == 3:
        down = dice_down.pop(0)
        up = dice_up.pop(1)
        dice_up.insert(1,down)
        dice_down.append(up)
    elif step == 4:
        down = dice_down.pop(2)
        up = dice_up.pop(1)
        dice_up.insert(1,down)
        dice_down.insert(0,up)

for s in step :
    if 0 > (y + dx[s]) or (y + dx[s]) > m-1 or 0 > (x + dy[s]) or (x + dy[s]) > n-1 :
        continue
    else:   
        y += dx[s]
        x += dy[s]

        dice_move(s)

        if arr[x][y] == 0 :
            arr[x][y] = dice_down[1]
        else :
            dice_down[1] = arr[x][y]
            arr[x][y] = 0

        print(dice_up[1])