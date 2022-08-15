def solution(s):
    cnt_zero = 0
    cnt_change = 0
    
    while s!='1' :
        num = s.count('1')        
        cnt_zero += len(s) - num       
        s = bin(num)[2:]
        cnt_change += 1
    
    return [cnt_change,cnt_zero]