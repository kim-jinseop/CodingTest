def solution(N, stages):
    p = len(stages)
    box = []
    for n in range(1,N+1) :
        if p:
            nc = stages.count(n)
            box.append((n,nc/p))
            p -= nc
        else :
            box.append((n,0))
    
    box = sorted(box,key=lambda x:x[1],reverse=True)

    result = [r for r,q in box]
    return  result