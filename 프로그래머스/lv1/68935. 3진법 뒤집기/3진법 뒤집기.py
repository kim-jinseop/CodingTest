def solution(n):
    box = []
    result = 0
    while n!=0 :
        box.append(n%3)
        n = n//3
    
    for i in range(len(box)) :        
        result += box.pop() * (3 ** i)  
    return result