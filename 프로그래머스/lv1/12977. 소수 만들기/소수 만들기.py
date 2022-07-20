from itertools import combinations

def solution(nums):
    combi = list(combinations(nums,3))
    cnt = 0

    box = [0] * 3001
    mino = []
    for i in range(2,3001) :
        if box[i]==0 :
            mino.append(i)
            for j in range(i,3001,i) :
                box[j] = 1

    for com in combi :
        if sum(com) in mino :
            cnt += 1 
    return cnt 