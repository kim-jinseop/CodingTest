def solution(n):
    box = [0] * (n+1)
    box[0] = 1
    box[1] = 1
    
    for i in range(2,n+1) :
        box[i] = (box[i-1] + box[i-2])%1000000007
        
    return box[n]

