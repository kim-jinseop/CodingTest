from itertools import combinations

def solution(numbers):
    answer = []
    
    data = list(combinations(numbers, 2))
    
    for i,j in data :
        answer.append(i+j)
        
    answer = sorted(list(set(answer)))
    
    
    return answer