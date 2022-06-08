data = [0] * 10001
def check(a) :
    return

def create(num) :
    fst_num = num
    str_num = str(num)
    sum = 0

    for i in str_num :
        sum += int(i)

    sum += fst_num

    if sum>10000 or sum<1 :
        return 0
    else :
        return sum

for num in range(1,10001) :
    sum = create(num)
    data[sum] = True


for i in range(10001) : 
    if data[i] == 0 :
        print(i)