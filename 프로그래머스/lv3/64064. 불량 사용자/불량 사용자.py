from itertools import permutations
def solution(user_id, banned_id):
    user_id = list(permutations(user_id,len(banned_id)))
    
    box = []
    for user in user_id :
        cnt = 0
        for index,ban in enumerate(banned_id) :
            if len(ban) != len(user[index]) :
                continue

            for i in range(len(ban)) :
                if not (ban[i]==user[index][i] or ban[i]=="*") :
                    break
            else :
                cnt += 1
                
        if cnt == len(banned_id) :
            if set(user) not in box : 
                box.append(set(user))
                
    return len(box)