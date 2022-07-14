from sys import stdin
from collections import deque

n,m = map(int,stdin.readline().split())
r,c,d = map(int,stdin.readline().split())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]

start = (r,c)
arr[r][c] = 2 

dx = [0,1,0,-1] 
dy = [-1,0,1,0]

def turn() :
    global d
    d -= 1
    if d < 0 :
        d = 3
        
def func(start) :
    global d
    queue = deque([start])
    cnt = 0
    result = 1
    
    while queue :
        s = queue.popleft()
        turn()        
        ny = s[0] + dy[d]
        nx = s[1] + dx[d]
        
        if arr[ny][nx] == 0 :
            queue.append((ny,nx))
            arr[ny][nx] = 2
            result += 1
            cnt = 0
        else :
            cnt +=1 
        
            if cnt == 4 :
                turn()
                turn()
                ny = s[0] + dy[d]
                nx = s[1] + dx[d]
                
                if arr[ny][nx] == 1 :
                    break
                else :
                    queue.append((ny,nx))
                    turn()
                    turn()
                    cnt = 0
            else :
                queue.append(s) 
                
    print(result)
    
func(start)