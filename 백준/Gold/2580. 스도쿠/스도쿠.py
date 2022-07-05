from re import L
import sys

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
zero_data = []
for i in range(9) :
    for j in range(9) :
        if arr[i][j] == 0 :
            zero_data.append((i,j))
zero_cnt = len(zero_data)

def sudoku_row(x,i) :
    for a in range(9) :
        if arr[x][a] == i :
            return False
    return True

def sudoku_colum(y,i) :
    for a in range(9) :
        if arr[a][y] == i :
            return False
    return True

def sudoku_3x3(x,y,i) :
    x_range = x//3 * 3
    y_range = y//3 * 3
    
    for a in range(x_range,x_range+3) :
        for b in range(y_range,y_range+3) :
            if arr[a][b] == i :
                return False
    return True

def backtracking(cnt) :
    if zero_cnt == cnt :
        for i in arr :
            print(*i)
        exit()
    
    for i in range(1,10) :
        x,y = zero_data[cnt]
        if sudoku_row(x,i) and sudoku_colum(y,i) and sudoku_3x3(x,y,i) :
            arr[x][y] = i
            backtracking(cnt+1)
            arr[x][y] = 0
    
backtracking(0) 