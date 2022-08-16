def solution(arr1, arr2):  
    answer = [[sum(i*j for i,j in zip(a,b)) for b in zip(*arr2)] for a in arr1]
    return answer