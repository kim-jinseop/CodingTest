def solution(n):
    answer = 0
    cnt = bin(n).count('1')
    i = 0
    while True :
        i += 1
        if cnt == bin(n+i).count('1') :
            answer = n+i
            break
    return answer