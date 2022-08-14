from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    arr = [0] * bridge_length
    q = deque(arr)
    Sum = 0
    
    while truck_weights :
        answer += 1
        Sum -= q.popleft()
        
        if Sum + truck_weights[0] <= weight :
            truck = truck_weights.pop(0)
            q.append(truck)
            Sum += truck
            
        else :
            q.append(0)
        
    answer += bridge_length
    return answer

