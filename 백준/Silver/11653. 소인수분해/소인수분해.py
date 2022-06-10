n = int(input()) 

i = 2

while True :    
    if n == 1 :
        break
    
    if n % i == 0 :
        print(i)
        n = n // i
        i = 1
        
    i += 1       