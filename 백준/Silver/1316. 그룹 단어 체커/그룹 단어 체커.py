n = int(input())
result = 0

for _ in range(n) :
    m = input()
    error = False 
    
    for index in range(len(m)-1) :
        if m[index] != m[index+1] :
            new_word = m[index+1:]

            if new_word.count(m[index]) > 0:
                error = True
                break
                
    if error == False :
        result += 1
        
print(result) 