def solution(name):
    answer = len(name)-1  # 좌우로 움직임의 최대값(A가 없을 경우)
    
    #좌우 움직임의 최솟값
    i = 1
    while i < len(name):
        if name[i] == 'A':
            R = i-1
            i += 1
            while i < len(name) and name[i] == 'A':
                i += 1
            L = len(name)-i
            answer = min([answer, 2*L + R, 2*R + L])
        else:
            i += 1

    for i in name :
        if i != 'A' :
            answer += min((ord('Z')-ord(i)+1),(ord(i)-ord('A')))

    return answer
