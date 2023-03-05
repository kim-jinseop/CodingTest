from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    for _,value in Counter(tangerine).most_common() :
        answer += 1
        k -= value
        if k <= 0 :
            break
    return answer