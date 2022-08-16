def solution(n):
    answer = 0
    box = [1] * (n+1)
    
    for i in range(2,n+1) :
        box[i] = (box[i-2] + box[i-1]) %1234567
    
    return box[n]