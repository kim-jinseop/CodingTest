from bisect import bisect_left
def solution(info, query):
    answer = []
    dict_info = {}
    
    #지원자 정리
    for i in info :
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])

        for a in [condition[0],'-'] :
            for b in [condition[1],'-'] :
                for c in [condition[2],'-'] :
                    for d in [condition[3],'-'] :
                        if a+b+c+d in dict_info :
                            dict_info[a+b+c+d].append(score)
                        else :
                            dict_info[a+b+c+d] = [score]
    
    #지원자 점수 오름차순 정렬 
    for di in dict_info.values():  
        di.sort()
        
    #조건 비교
    query = [x.replace(" and ","").split() for x in query]
    
    for q in query :
        if q[0] in dict_info :
            answer.append(len(dict_info[q[0]]) - bisect_left(dict_info[q[0]],int(q[1])))
        else :
            answer.append(0)
        
    return answer