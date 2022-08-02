def solution(phone_book):
    arr = sorted(phone_book)

    for i in range(len(arr)-1) :
        leng = len(arr[i])
        if arr[i] == arr[i+1][:leng] :
            return False
            
    return True