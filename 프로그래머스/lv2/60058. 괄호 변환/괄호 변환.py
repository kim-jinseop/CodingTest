def func(p) :
    u = ''            
    v = ''
    new = ''
    
    #split u,v
    if p=='' :
        return ''
    
    for i in range(0,len(p)-1,2) :
        if len(p) >= 1 :
            u += p[i:i+2]
    
            if u.count('(') == u.count(')') :
                v += p[i+2:]
                break 
        else :
            v += p

    #chk u
    chk = u
    while True :
        if chk.find('()') != -1 :
            chk = chk.replace('()','')
        else :
            break

    if chk != '':
        return '(' + func(v) + ')' + ''.join(['(' if x==')' else ')' for x in u[1:-1]])
    else :
        return u + func(v)

def solution(p):
    answer = '' 
    answer += func(p)
    return answer