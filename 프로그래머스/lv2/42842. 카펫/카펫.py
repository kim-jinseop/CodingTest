def solution(brown, yellow):
    answer = []
    divisor = []
    
    for i in range(1,int(yellow**0.5)+1) :
        if yellow%i == 0 :
            divisor.append((yellow//i,i))
    
    while divisor :
        x = divisor.pop(0)
        if brown + yellow == (x[0] + 2) * (x[1] + 2) :
            answer.append([x[0]+2,x[1]+2])
            break
            
    return answer[0]