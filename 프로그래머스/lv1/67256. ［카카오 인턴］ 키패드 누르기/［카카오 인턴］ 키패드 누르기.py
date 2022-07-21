def solution(numbers, hand):
    data = [[1,4,7,'*'],[2,5,8,0],[3,6,9,'#']]
    l_posi = (0,3)
    r_posi = (2,3)
    answer = ''
    
    for num in numbers :
        if num in data[0] :
            l_posi = (0,data[0].index(num))
            answer += 'L'
        elif num in data[2] :
            r_posi = (2,data[2].index(num))
            answer += 'R'
        else :
            s_posi = (1,data[1].index(num))

            if abs(s_posi[0]-l_posi[0]) + abs(s_posi[1]-l_posi[1]) < abs(s_posi[0]-r_posi[0]) + abs(s_posi[1]-r_posi[1]) :
                l_posi = s_posi
                answer += 'L'
            elif abs(s_posi[0]-l_posi[0]) + abs(s_posi[1]-l_posi[1]) > abs(s_posi[0]-r_posi[0]) + abs(s_posi[1]-r_posi[1]) :
                r_posi = s_posi
                answer += 'R'
            else :
                if hand == "right" :
                    r_posi = s_posi
                    answer += 'R'
                else :
                    l_posi = s_posi
                    answer += 'L'
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))