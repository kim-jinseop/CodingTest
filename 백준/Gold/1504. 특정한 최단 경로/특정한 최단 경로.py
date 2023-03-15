from sys import stdin
import heapq

n, e = map(int,stdin.readline().split())
distance_v1 = [int(1e9)] * (n+1)
distance_v2 = [int(1e9)] * (n+1)

grape = [[] for _ in range(n+1)]
for _ in range(e) :
    a,b,c = map(int,stdin.readline().split())
    grape[a].append((b,c))
    grape[b].append((a,c))
v1, v2 = map(int,stdin.readline().split())


def dijkstra(start,distance) :
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        if distance[now] < dist :
            continue

        for i in grape[now] :
            cost = dist + i[1]

            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))

dijkstra(v1,distance_v1)
dijkstra(v2,distance_v2)

result = min(distance_v1[1] + distance_v1[v2] + distance_v2[n],
          distance_v2[1] + distance_v2[v1] + distance_v1[n])

if result >= int(1e9) :
    print(-1)
else : 
    print(result)