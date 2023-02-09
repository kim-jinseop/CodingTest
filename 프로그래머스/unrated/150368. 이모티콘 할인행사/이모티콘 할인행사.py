from itertools import product 
# 중복 순열

def solution(users, emoticons):
    answer = []
    sales = list(product([10,20,30,40], repeat=len(emoticons)))

    for sale in sales :
        m = 0
        s = 0
        for user in users :
            buy, money = user
            total = 0

            for i in range(len(emoticons)) :
                if buy <= sale[i] :
                    total += emoticons[i] * (100-sale[i]) /100
                
            if money <= total :
                m += 1
            else :
                s += total
            
        answer.append([m,s])
        
    answer.sort()
    return answer[-1]
