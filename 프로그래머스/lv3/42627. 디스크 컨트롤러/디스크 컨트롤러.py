def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[1])
    real_time = 0
    num = len(jobs)

    while jobs :
        for i in range(len(jobs)) :
            if jobs[i][0] <= real_time :
                job = jobs.pop(i)
                real_time += job[1]
                answer += real_time - job[0]
                break 
        else :
             real_time += 1
                
    return answer//num