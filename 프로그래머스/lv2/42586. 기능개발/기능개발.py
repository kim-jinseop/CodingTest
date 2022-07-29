def solution(progresses, speeds):
    answer = []
    day = 0

    while progresses :
        day += 1
        
        for i in range(len(progresses)) :
            progresses[i] += speeds[i]
            
        cnt = 0
        while progresses :
            if progresses[0] > 99 :
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else :
                break
                
        if cnt>0 :
            answer.append(cnt)
            
    return answer