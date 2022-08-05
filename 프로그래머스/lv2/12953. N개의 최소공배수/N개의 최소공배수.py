import math
def solution(arr):
    answer = 1 
    
    while len(arr) > 1 : 
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b // math.gcd(a,b))
    answer = arr[0]
    return answer