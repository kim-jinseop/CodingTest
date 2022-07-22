def solution(s):
    answer = ''

    for x in list(s.split(' ')) :
        for i,j in enumerate(x) :
            if i%2 == 0 :
                answer += j.upper()
            else :
                answer += j.lower()
        answer += ' '
        
    return answer[:-1]