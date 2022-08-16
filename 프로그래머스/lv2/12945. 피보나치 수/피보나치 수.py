# def solution(n):
#     box = [0] * (n+1)
#     box[1] = 1
    
#     for i in range(2,n+1) :
#         box[i] = (box[i-1] + box[i-2]) %1234567
#     return box[n]


def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,(a+b)%1234567
    return a
