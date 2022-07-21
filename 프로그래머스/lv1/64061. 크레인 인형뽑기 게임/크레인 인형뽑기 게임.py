def solution(board, moves):
    box = []
    result = 0
    for m in moves :
        for part in board :
            if part[m-1] > 0 :
                box.append(part[m-1])
                part[m-1] = 0
            
                if len(box) > 1 :
                    if box[-1] == box[-2] :
                        box.pop()
                        box.pop()
                        result += 2     
                break
    return result