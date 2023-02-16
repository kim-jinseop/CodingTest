from itertools import chain

def solution(board, skill):
    answer = 0

#     for s in skill :
#         t, r1, c1, r2, c2, degree = s
        
#         if t==1 : #공격
#             for i in range(r1, r2+1) :
#                 for j in range(c1, c2+1) :
#                     board[i][j] -= degree
            
#         else : #회복
#             for i in range(r1, r2+1) :
#                 for j in range(c1, c2+1) :
#                     board[i][j] += degree
    
#     ans = [x for x in chain(*board) if x>0]
#     return len(ans)
    
    box = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for s in skill :
        t, r1, c1, r2, c2, degree = s
        
        if t==1 : #공격
            box[r1][c1] -= degree
            box[r2+1][c1] += degree
            box[r1][c2+1] += degree
            box[r2+1][c2+1] -= degree
            
        else : #회복
            box[r1][c1] += degree
            box[r2+1][c1] -= degree
            box[r1][c2+1] -= degree
            box[r2+1][c2+1] += degree

    for i in range(0,len(box)) :
        for j in range(1,len(box[0])) :
            box[i][j] += box[i][j-1]
            
    for i in range(0,len(box[0])) :
        for j in range(1,len(box)) :
            box[j][i] += box[j-1][i]

    for i in range(0,len(board)) :
        for j in range(0,len(board[0])) :
            board[i][j] += box[i][j]
            
    ans = [x for x in chain(*board) if x>0]
    return len(ans)