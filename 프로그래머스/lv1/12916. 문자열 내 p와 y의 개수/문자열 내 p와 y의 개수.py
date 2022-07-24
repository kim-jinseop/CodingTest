def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y') :
        answer = True
    else :
        if ('p' in s) or ('y' in s) :
            answer = False
        else :
            answer = True 
            
    return answer