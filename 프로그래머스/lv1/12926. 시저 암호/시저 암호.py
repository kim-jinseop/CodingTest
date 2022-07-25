def solution(s, n):
    result = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    ALP = alp.upper()
    
    for i in s :
        if i==' ' :
            result += ' '
        elif i.isupper() :
            result += ALP[(ALP.find(i) + n)%26]
        else :
            result += alp[(alp.find(i) + n)%26]
            
    return result 