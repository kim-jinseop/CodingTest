def solution(a, b):
    week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    cnt = 0
    
    total = sum(day[0:a-1]) + b - 1 
    
    answer = week[total%7 - 2]
    return answer