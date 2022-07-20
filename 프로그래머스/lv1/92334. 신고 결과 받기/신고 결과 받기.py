def solution(id_list, report, k):
    result = [0] * len(id_list)
    r_report = {x : 0 for x in id_list}
    set_report = set(report)
    
    for i in set_report :
        r_report[i.split()[1]] += 1
    
    for i in set_report :
        if r_report[i.split()[1]] >= k :
            result[id_list.index(i.split()[0])] += 1
    
    return result