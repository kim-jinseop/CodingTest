from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course :
        all_combi = []
        for order in orders :
            all_combi += list(combinations(sorted(order),c))
            
        box = Counter(all_combi).most_common()
        for key,value in box :
            if value == Counter(all_combi).most_common(1)[0][1] and value > 1:
                answer.append(''.join(key))
            
    return sorted(answer)