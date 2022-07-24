def solution(n):
    answer = []
    result = [0] * (n+1)
    for i in range(2,n+1) :
        if result[i] == 0:
            answer.append(i)
            for j in range(i,n+1,i) :
                result[j] = 1
    
    return len(answer)