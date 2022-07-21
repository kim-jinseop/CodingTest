def solution(array, commands):
    result = []
    for part in commands :
        i,j,k = part
        
        arr = sorted(array[i-1:j])
        result.append(arr[k-1])

    return result