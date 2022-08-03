def solution(sizes):

    cbox = []
    rbox = []
    for c,r in sizes :
        if c<r :
            c,r = r,c
        cbox.append(c)
        rbox.append(r)
            
    answer = max(cbox) * max(rbox)

    return answer