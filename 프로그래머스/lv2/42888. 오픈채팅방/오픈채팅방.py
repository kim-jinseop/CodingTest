def solution(record):
    idbox = {}
    keybox = []
    answer = []
    for part in record :
        if part[0] == 'E' :
            k,ID,name = part.split()
            idbox[ID] = name
            keybox.append((k,ID))
        elif part[0] == 'L' :
            k,ID = part.split()
            keybox.append((k,ID))
        else :
            k,ID,name = part.split()
            idbox[ID] = name
    
    for i in keybox :
        if i[0] == 'Enter' :
            answer.append("{}님이 들어왔습니다.".format(idbox[i[1]]))
        else :
            answer.append("{}님이 나갔습니다.".format(idbox[i[1]]))
            
    return answer