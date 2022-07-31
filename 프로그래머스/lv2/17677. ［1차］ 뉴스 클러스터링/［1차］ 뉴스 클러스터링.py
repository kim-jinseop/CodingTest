def solution(str1, str2):
    box1 = []
    box2 = []
    answer = 0
    
    # upper -> lower
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 2 split
    for i in range(len(str1)-1) :
        box1.append(''.join(str1[i:i+2]))
    for i in range(len(str2)-1) :
        box2.append(''.join(str2[i:i+2]))
    
    # alpha chk
    for i in box1[:] :
        if not i.isalpha() :
            box1.remove(i)
    for i in box2[:] :
        if not i.isalpha() :
            box2.remove(i)
    
    if not box1 and not box2 :
        return 65536
        
    # &, |
    g = set(box1) & set(box2)
    h = set(box1) | set(box2)
    gbox = []
    hbox = []
    print(g)
    
    for i in g :
        for j in range(min(box1.count(i),box2.count(i))) :
            gbox.append(i)
            
    for i in h :
        for j in range(max(box1.count(i),box2.count(i))) :
            hbox.append(i)
            
    return int(len(gbox)/len(hbox) * 65536)