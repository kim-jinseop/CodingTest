def solution(survey, choices):
    dic = {'R':0,'C':0, 'J':0, 'A':0,'T':0,'F':0, 'M':0, 'N':0}
    grade = [-3,-2,-1,0,1,2,3]
    answer = []
    
    for i in range(len(survey)) :
        g = grade[choices[i]-1]
        
        if g<0 :
            dic[survey[i][0]] -= g
        elif g>0 :
            dic[survey[i][1]] += g
            
    if dic['R'] >= dic['T'] :
        answer.append('R')
    else :
        answer.append('T')
        
    if dic['C'] >= dic['F'] :
        answer.append('C')
    else :
        answer.append('F')     
           
    if dic['J'] >= dic['M'] :
        answer.append('J')
    else :
        answer.append('M')
        
    if dic['A'] >= dic['N'] :
        answer.append('A')
    else :
        answer.append('N')
    
    return ''.join(answer)