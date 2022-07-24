def solution(dartResult):
    box = []
    
    for i in dartResult :
        if i.isdigit() :
            if len(box) > 0 and box[-1] == 1 and i == '0' :
                box[-1] = 10
            else :
                box.append(int(i))
        elif i=='S' or i=='D' or i=='T' :
            if i=='D' :
                box[-1] = box[-1] ** 2
            elif i=='T' :
                box[-1] = box[-1] ** 3
        else :
            if i=='*' :
                box[-1] = box[-1] * 2
                if len(box) > 1 :
                    box[-2] = box[-2] * 2
            else :
                box[-1] = -box[-1]
            
    return sum(box)