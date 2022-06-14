a,b = input().split()
a_list = [0] * 3 
b_list = [0] * 3 

for i in range(len(a)) :
    a_list[i] = a[2-i]
    b_list[i] = b[2-i]
    
a_list = ''.join(a_list)
b_list = ''.join(b_list) 

if a_list>b_list :      
    print(a_list)
else :
    print(b_list)