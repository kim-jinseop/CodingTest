n = int(input())
count = 0
num = n

while True :
    count += 1

    if num < 10 :
        save = num
        num = num * 10
        num += save

    else :
        fst_num = num//10
        sec_num = num%10

        num = (sec_num * 10) + ((fst_num + sec_num)%10)

    if num == n :
        break
    

print(count)