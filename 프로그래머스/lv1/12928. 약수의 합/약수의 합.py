def solution(n):
    answer = []
    if n==0 : 
        return 0
    
    for i in range(1,int(n**0.5)+1) :
        if n%i==0 :
            answer.append(i)
            answer.append(n/i)
            
    return sum(set(answer))