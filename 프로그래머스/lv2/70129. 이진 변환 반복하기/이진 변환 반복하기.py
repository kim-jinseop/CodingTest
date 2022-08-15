def solution(s):
    answer = []
    cnt_zero = 0
    cnt_change = 0
    
    while s!='1' :
        b_leng = len(s)
        s = s.replace('0','')
        a_leng = len(s)
        
        cnt_zero += b_leng-a_leng
        
        s = bin(a_leng)[2:]
        cnt_change += 1
    
    answer.append(cnt_change)
    answer.append(cnt_zero)
    return answer