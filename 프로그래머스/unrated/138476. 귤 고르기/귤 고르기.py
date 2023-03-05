from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    d = defaultdict(int)
    
    for i in tangerine :
        d[i] += 1
    
    d = sorted(d.items(),key=lambda item: item[1], reverse=True)

    for _, i in d :
        answer += 1 
        k -= i
        if k<=0 :
            break
    return answer