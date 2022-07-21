def solution(a, b):
    Sum = 0
    for i in range(len(a)) :
        Sum += a[i] * b[i]
    return Sum