import copy 
def solution(land):
    answer = 0
    
    for idx in range(len(land)-1) :
        #case1
        mi = land[idx].index(max(land[idx]))
        x = land[idx].pop(mi) # 1st
        y = land[idx].pop(land[idx].index(max(land[idx]))) # 2en
        
        for i in range(4) :
            if i == mi : 
                land[idx+1][i] += y
            else :
                land[idx+1][i] += x
    
    return max(land[len(land)-1])