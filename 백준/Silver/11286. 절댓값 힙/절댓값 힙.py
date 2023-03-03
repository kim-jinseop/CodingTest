from sys import stdin
import heapq

hq = []
n = int(stdin.readline())
for _ in range(n) :
    x  = int(stdin.readline())

    if x != 0 :
        heapq.heappush(hq, (abs(x), x) )
    else : 
        if hq :
            result = heapq.heappop(hq)
            print(result[1])
        else : 
            print(0)



