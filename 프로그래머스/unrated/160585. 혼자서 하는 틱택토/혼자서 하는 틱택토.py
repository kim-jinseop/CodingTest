def solution(board):
    win_o = 0
    win_x = 0
    
    # 개수 확인
    cnt_o = 0 
    cnt_x = 0
    for line in board :
        for i in line :
            if i == "O" :
                cnt_o += 1                
            elif i == "X" :
                cnt_x += 1
                
    if cnt_o-cnt_x != 0 and cnt_o-cnt_x != 1:
        return 0
    
    # 세로가 3칸으로 완성되어 있는 경우

    board_t = list(zip(*board))
    for b in board_t :
        if b == ("O","O","O") :
            win_o += 1
        if b == ("X","X","X") :
            win_x += 1

    # 가로가 3칸으로 완성되어 있는 경우
    for b in board :
        if b == ("OOO") :
            win_o += 1

        if b == ("XXX") :
            win_x += 1
   
    # 대각선이 완성되어 있는 경우
    if board[0][0] == board[1][1] == board[2][2] :
        if board[1][1] == "O" :
            win_o += 1
        elif board[1][1] == "X" :
            win_x += 1
    if board[0][2] == board[1][1] == board[2][0] :
        if board[1][1] == "O" :
            win_o += 1
        elif board[1][1] == "X" :
            win_x += 1
            
    if win_o == 2 and win_x == 0 and cnt_o > cnt_x:
        return 1
    elif win_o + win_x > 1:
        return 0
    elif win_x == 1 and cnt_o > cnt_x:
        return 0
    elif win_o == 1 and cnt_o == cnt_x:
        return 0
    
    return 1


# 가능조건
# 3칸이 완성되어 있으면 안됨
# 개수를 확인 했을 때 X가 먼저 등장하면 안됨