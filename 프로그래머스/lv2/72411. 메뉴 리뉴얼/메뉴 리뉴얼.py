from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course :
        tbox = {}
        sbox = set()
        
        for i in orders :
            if len(i) >= c :
                sbox.update(list(combinations(sorted(i), c)))
        cou = sorted(sbox)

        for i in cou :
            tbox[''.join(i)] = 0 
            for j in orders :
                if set(i).issubset(set(j)) :
                    tbox[''.join(i)] += 1
        
        if tbox :
            Max = max(tbox.values())
        
        for key,value in tbox.items() :
            if Max == value and Max > 1:
                answer.append(key)
                    
    return sorted(answer)