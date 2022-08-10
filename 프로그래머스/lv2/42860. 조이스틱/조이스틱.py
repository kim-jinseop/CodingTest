def solution(name) :
    answer = 0
    Min = len(name)
    #상하
    for i in name :
        if i != "A" :
            answer += min((ord('Z')-ord(i)+1),(ord(i)-ord('A')))
    
    leng = len(name)
    #좌우
    for i in range(leng):
        index = i + 1
        while index<leng and name[index] == 'A' :
            index += 1
            
        Min = min(Min, i*2+leng-index,2*(leng-index)+i)
        
    answer += Min
    return answer