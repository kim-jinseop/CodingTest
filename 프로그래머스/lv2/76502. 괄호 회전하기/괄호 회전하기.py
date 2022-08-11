def solution(s):
    chk = 0
    
    test = s
    for i in range(len(s)) :
        while ('[]' in test) or ('()' in test) or ('{}' in test) :
            test = test.replace('[]','')
            test = test.replace('{}','')
            test = test.replace('()','')
        
        if test=='' :
            chk += 1
            
        test = s[i+1:] + s[:i+1]
        
    return chk