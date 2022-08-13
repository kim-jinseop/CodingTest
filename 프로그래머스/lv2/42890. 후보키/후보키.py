from itertools import combinations

def solution(relation):
    answer = []
    arr = list(zip(*relation))
    num = [i for i in range(len(arr))]
    
    for i in range(1,len(arr)+1) :
        combination = list(combinations(num,i))
        
        for combi in combination :
            if len(set(map(''.join,zip(*[arr[index] for index in combi])))) == len(relation) :
                for a in answer :
                    if set(a).issubset(set(combi)) :
                        break
                else :
                    answer.append(combi)
    return len(answer)
