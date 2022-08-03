from itertools import permutations
def solution(numbers):
    answer = 0
    box = set()
    for i in range(len(numbers)) :
        box |= set(map(int,map(''.join,permutations(numbers,i+1))))
    
    box -= set(range(0,2))
    Max = max(box)
    
    data = [0] * (Max+1)
    for i in range(2, Max+1):
        if data[i] == 0 :
            for j in range(i*2,Max+1,i) :
                data[j] = 1
    
    for part in box :
        if data[part] == 0 :
            answer += 1
            
    return answer