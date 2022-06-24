import sys
In = sys.stdin.readline

def binary_search(arr, target, start, end) :
    if start > end :
        return None 
    
    mid = (start+end) // 2
    
    if target == arr[mid] :
        return arr[mid]
    elif target > arr[mid] :
        return binary_search(arr, target, mid+1, end)
    elif target < arr[mid] :
        return binary_search(arr, target, start, mid-1)
    
n = int(In())
data_have = sorted(list(map(int,In().split())))
m = int(In())
data_field = list(map(int,In().split()))

for i in data_field :
    if binary_search(data_have, i, 0, n-1) :
        print(1, end=' ')
    else :
        print(0, end=' ')