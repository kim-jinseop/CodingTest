def solution(n):
    answer = ''
    while n :
        mod = n%3
        n = n//3
        
        if mod == 0 :
            n -= 1
            mod = 3
            
        answer += str(mod)
        
    return answer[::-1].replace('3','4')