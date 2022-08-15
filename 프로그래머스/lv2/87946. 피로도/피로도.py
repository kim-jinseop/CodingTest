from itertools import permutations

def solution(k, dungeons):
    answer = -1
    save = k
    dungeons = list(permutations(dungeons,len(dungeons)))
    
    for dungeon in dungeons :
        cnt = 0
        for m,s in dungeon:
            if k >= m :
                k -= s
                cnt += 1
        k = save
        answer = max(answer,cnt)
        
    return answer