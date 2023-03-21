def solution(board):
    INF = int(1e9)
    answer = 0
    
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    w = len(board[0])
    h = len(board)
    
    visit = [[-1] * w for _ in range(h)]
    print(visit)
    def func(x,y,cnt) :        
        for i in range(4) :
            nx = dx[i] + x
            ny = dy[i] + y
            while True :
                if nx>=h or nx<0 or ny>=w or ny<0 or board[nx][ny] == "D":
                    nx -= dx[i]
                    ny -= dy[i] 
                    break
                else : 
                    nx += dx[i]
                    ny += dy[i] 

            if visit[nx][ny] == -1 or visit[nx][ny] > cnt+1 :
                visit[nx][ny] = cnt+1
                func(nx,ny,cnt+1)
    
    for i in range(h) :
        for j in range(w) :
            if board[i][j] == "R" :
                visit[i][j] = 0
                func(i,j,0)
                
            elif board[i][j] == "G" :
                save = (i,j)
                
    return visit[save[0]][save[1]]