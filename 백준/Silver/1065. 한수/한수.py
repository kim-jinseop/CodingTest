n = int(input())
result = 0

for num in range(1,n+1) :
    if num<100 :
        result += 1
    else :
        str_num = str(num)

        fst_sub = int(str_num[0]) - int(str_num[1])
        sec_sub = int(str_num[1]) - int(str_num[2])
        
        if fst_sub == sec_sub :
            result += 1

print(result)