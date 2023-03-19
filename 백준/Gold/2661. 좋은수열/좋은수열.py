from sys import stdin
leng = int(stdin.readline())

def func(arr) :
    if len(arr) == leng :
        print(arr)
        exit(0)
    
    for i in "123" : 
        new_arr = arr + i

        for j in range(1, len(new_arr)//2+1):
            if new_arr[-j:] == new_arr[-2*j:-j]:
                break
        else :
            func(new_arr)

func("")