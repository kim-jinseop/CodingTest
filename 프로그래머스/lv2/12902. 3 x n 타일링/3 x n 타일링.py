def solution(n):
    box = [0] * (n+1)
    box[2] = 3
    box[4] = 11
    
    for i in range(6,n+1,2) :
        box[i] = (4*box[i-2] - box[i-4]) % 1000000007
        
    return box[n] 