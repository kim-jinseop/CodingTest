import copy

def solution(array, commands):
    result = []
    for part in commands :
        i,j,k = part
        
        arr = array[i-1:j]
        arr.sort()
        
        result.append(arr[k-1])

    return result