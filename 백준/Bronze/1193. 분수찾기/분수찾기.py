n = int(input())
i = 0 

mother = 0
son = 0

while n > 0 :
    i += 1 
    n -= i
    
if i%2 == 1 : # 홀수
    mother = i + n
    son = 1 - n
    
else :        # 짝수
    mother = 1 - n
    son = i + n 
    
print(f'{son}/{mother}')