a = input().upper()
b = set(a)
max_count = 0

for i in b :
    f_count = a.count(i)
    f_chr = i   
    
    if max_count < f_count :
        max_count = f_count
        result = i
    
    elif max_count == f_count :
        result = '?'
            
print(result)