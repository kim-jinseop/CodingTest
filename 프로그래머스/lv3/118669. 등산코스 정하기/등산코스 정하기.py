import heapq

def solution(n, paths, gates, summits):
    answer = []
    INF = int(1e9)
    graph = [[] for i in range(n+1)]
    gates = set(gates)
    summits = set(summits)
    for a,b,c in paths :
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    for gate in gates :
        MAX = 0
        q = []
        distance = [INF] * (n+1)
        heapq.heappush(q, (0, gate))
        distance[gate] = 0

        while q :
            dist, now = heapq.heappop(q)

            if distance[now] < dist :
                continue
            if MAX < dist : 
                MAX = dist
            if now in summits :
                answer.append((now, MAX))
                break

            for gn, gd in graph[now] : 
                if gd < distance[gn] and gn not in gates:
                    distance[gn] = gd
                    heapq.heappush(q, (gd, gn))

    return sorted(answer, key = lambda x : (x[1],x[0]))[0]
