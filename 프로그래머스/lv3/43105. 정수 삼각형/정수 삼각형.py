def solution(triangle):
    answer = 0
    
    # box = [[0 for _ in arr] for arr in triangle]
    # box[0][0] = triangle[0][0]
    
    for i in range(len(triangle)-1,-1,-1) :
        for j in range(len(triangle[i])-1) :
            triangle[i-1][j] += max(triangle[i][j], triangle[i][j+1])
    
    return triangle[0][0]