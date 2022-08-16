def solution(files):
    box = []
    
    for file in files :
        head = ''
        number = ''
        tail = ''
        
        for i in range(len(file)) :
            if file[i].isdigit() :
                head += file[:i]
                index = i
                break
                
        for i in range(index,len(file)) :
            if file[i].isdigit() :   
                number += file[i]
            else :
                tail += file[i:]
                break
                
        box.append((head,number,tail))
        
    box = sorted(box,key=lambda x:(x[0].lower(),int(x[1])))
    answer = list(map(''.join,box))
    return answer