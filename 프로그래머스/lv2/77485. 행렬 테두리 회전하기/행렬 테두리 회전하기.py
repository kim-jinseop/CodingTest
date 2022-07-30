import numpy as np

def lotate(matrix, q) :
    x1,y1,x2,y2 = q
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    box = []
    for i in range(y2,y1,-1) :
        matrix[x1][i],matrix[x1][i-1] = matrix[x1][i-1],matrix[x1][i]
        box.append(matrix[x1][i])
        box.append(matrix[x1][i-1])

    for i in range(x1,x2) :
        matrix[i][y1],matrix[i+1][y1] = matrix[i+1][y1],matrix[i][y1]
        box.append(matrix[i][y1])
        box.append(matrix[i+1][y1])

    for i in range(y1,y2) :
        matrix[x2][i],matrix[x2][i+1] = matrix[x2][i+1],matrix[x2][i]
        box.append(matrix[x2][i])
        box.append(matrix[x2][i+1])
        
    for i in range(x2,x1+1,-1) :
        matrix[i][y2],matrix[i-1][y2] = matrix[i-1][y2],matrix[i][y2]
        box.append(matrix[i][y2])
        box.append(matrix[i-1][y2])
        
    Min = min(set(box))
    return matrix, Min

def solution(rows, columns, queries):
    answer = []
    matrix = np.arange(1,rows*columns+1).reshape(rows,columns).tolist()

    for q in queries :
        matrix,Min = lotate(matrix, q)
        answer.append(Min)
    
    return answer
