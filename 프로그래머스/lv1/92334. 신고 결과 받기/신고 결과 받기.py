def solution(id_list, report, k):
    r_report = {}
    t_report = {}
    stop_id = []
    result = [0] * len(id_list)
    
    for i in id_list :
        r_report[i] = 0
        t_report[i] = []
        
    for i in report :
        a,b = i.split()
        
        if (b in t_report[a]) == False :
            r_report[b] += 1
            t_report[a].append(b)
        
            if r_report[b] == k :
                stop_id.append(b)
            
    for i in range(len(id_list)) :
        for j in stop_id :
            if j in t_report[id_list[i]] :
                result[i] += 1
        
    return result