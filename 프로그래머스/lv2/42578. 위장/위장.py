def solution(clothes):
    answer = 1
    box = {}
    
    for cloth in clothes :
        if cloth[1] in box :
            box[cloth[1]].append(cloth[0])
        else :
            box[cloth[1]] = [cloth[0]]
    
    for value in box.values() :
        answer *= len(value)+1
        
    return answer - 1