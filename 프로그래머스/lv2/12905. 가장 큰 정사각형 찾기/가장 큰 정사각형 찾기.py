def solution(board):
    answer = 0
    for i in range(1,len(board)) :
        for j in range(1,len(board[0])) :
            if board[i][j] == 1 :
                board[i][j] = min(board[i][j-1], board[i-1][j], board[i-1][j-1]) + 1
    
    Max = max([max(part) for part in board])
    return Max**2