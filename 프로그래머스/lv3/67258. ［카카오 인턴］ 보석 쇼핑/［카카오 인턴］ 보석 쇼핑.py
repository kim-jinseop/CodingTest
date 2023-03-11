from collections import defaultdict

def solution(gems):    
    set_gems = set(gems)
    box = defaultdict(int)
    answer = [0,100000000]
    
    e = 0
    for s in range(len(gems)) :
        while e<len(gems) :
            if len(box) != len(set_gems) :
                box[gems[e]] += 1
                e += 1
            else :
                break
            
        if len(box) == len(set_gems) :
            answer = [s+1,e] if e-(s+1) < answer[1] - answer[0] else answer

        if box[gems[s]] - 1 == 0 :
            del(box[gems[s]])
        else : 
            box[gems[s]] -= 1
    
    return answer