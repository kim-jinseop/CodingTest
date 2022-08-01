def solution(s):
    answer = []
    box = list(s[2:-2].replace('},{',' ').split())
    intbox = []
    for b in box :
        intbox.append(set(map(int,b.split(','))))

    intbox = sorted(intbox, key=lambda x : len(x))
    answer.append(*intbox[0])
    
    for i in range(0,len(intbox)-1) :
        answer.append(*(intbox[i+1] - intbox[i]))
    return answer