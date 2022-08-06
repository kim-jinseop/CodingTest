import math
def solution(arr):
    answer = 1 
    
    while len(arr) > 1 : 
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b // math.gcd(a,b))
    answer = arr[0]
    return answer

# 공배수 하나를 구하고 구한 공배수와 다른수위 공배수를 구하면 여러개의 값의 공배수 구할 수 있음 
