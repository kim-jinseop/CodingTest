import heapq

def dijkstra(start,arr) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    
    while q :
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist :
            continue
        
        for i in arr[now] : # i[0] : end  i[1] : value
            cost = dist + i[1]
            
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
            
def solution(N, road, K):
    INF = int(1e9)
    global distance 
    distance = [INF] * (N+1) 
    answer = 0
    arr = [[] for _ in range(N+1)]
    
    for i in road :
        start,end,value = i
        arr[start].append((end,value))
        arr[end].append((start,value))
    
    dijkstra(1,arr)
    print(arr)
    for i in distance :
        if i<=K :
            answer += 1
            
    return answer