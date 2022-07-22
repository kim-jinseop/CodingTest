def solution(left, right):
    Sum = 0 
    for x in range(left,right+1) :
        if (x**0.5).is_integer() :
            Sum -= x
        else :
            Sum += x
            
    return Sum