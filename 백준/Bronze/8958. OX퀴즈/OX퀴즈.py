n = int(input())

for i in range(n) :
    text = input()
    num = 1
    result = 0

    for j in text :
        if j == 'O' :
            result += num
            num += 1
        else :
            num = 1
    print(result)