def solution(begin, end):
    box = []
    
    for i in range(begin,end+1) :
        x = 1
        for j in range(2,int(i**0.5)+1) :
            if i%j == 0 :
                if i//j > 10000000 :
                    x = 1
                    continue
                else :
                    x = i//j
                    break
                    
        box.append(x)
    if begin == 1 :
        box[0] = 0
        
    return box