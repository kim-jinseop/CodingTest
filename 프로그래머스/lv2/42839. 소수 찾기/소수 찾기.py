from itertools import permutations
def solution(numbers):
    answer = 0
    box = []
    calbox = []
    
    for i in range(1,len(numbers)+1) :
        box.extend(permutations(numbers,i))
        
    for i in box[:] :
        if i[0] == '0' :
            box.remove(i)
        else :
            calbox.append(int(''.join(i)))
    
    calbox = set(calbox)
    Max = max(calbox)
    
    data = [0] * (Max+1)
    data[0] = 1
    data[1] = 1
    for i in range(2, Max+1):
        if data[i] == 0 :
            for j in range(i*2,Max+1,i) :
                data[j] = 1
    
    for part in calbox :
        if data[part] == 0 :
            answer += 1
            
    return answer