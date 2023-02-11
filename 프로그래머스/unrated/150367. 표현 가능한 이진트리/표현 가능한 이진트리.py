def chk(dp, depth, nb) :
    if dp==depth :
        return True
    
    middle = len(nb) // 2 
    
    if nb[middle] == '1' :
        if (chk(dp+1, depth, nb[:middle]) and chk(dp+1, depth, nb[middle+1:])) == True :
            return True
        else : 
            return False
        
    elif nb[middle] == '0' :
        if '1' in nb :
            return False 
        else :
            return True


def solution(numbers):
    answer = []
    
    for num in numbers :
        b = bin(num)[2:]
        depth = 0
        while len(b) > 2**depth - 1 :
            depth += 1
        
        nb = '0' * ((2**depth-1)-len(b)) + b
        
        c = chk(1, depth, nb)
        
        if c == True : 
            answer.append(1)
        else : 
            answer.append(0)
            
    return answer