import math

while True :
    data = list(map(int,input().split()))
    if data[0] == 0 and data[1] == 0 and data[2] == 0:
        break

    data.sort()
    
    if data[0]**2 + data[1]**2 == data[2]**2 :
        print('right')
    else:
        print('wrong')