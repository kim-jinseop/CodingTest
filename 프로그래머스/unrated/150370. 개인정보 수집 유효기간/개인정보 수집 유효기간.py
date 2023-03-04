from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    ty , tm , td = map(int,today.split("."))
    t = defaultdict(int)
    for term in terms :
        c, m = term.split(" ")
        t[c] = int(m)
        
    for i,privacie in enumerate(privacies) : 
        privacie, pc = privacie.split(" ")
        py,pm,pd = map(int,privacie.split("."))
        
        year, month  = t[pc]//12, t[pc]%12 
        
        pm = pm + month
        if pm>12 :
            pm -= 12
            year += 1
        py = py + year
        
        if ty > py or (ty==py and tm > pm) or (ty==py and tm==pm and td >= pd) :
            answer.append(i+1)
        
        
    return answer