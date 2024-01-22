import math

def vector_length(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def solve(points):
    N = len(points)
    half = N // 2
    points_sum = [sum(x) for x in zip(*points)]
    min_length = float('inf')

    def dfs(idx, count, v1, v2):
        nonlocal min_length
        if idx == N:
            if count == half:
                v = [points_sum[0] - 2*v1, points_sum[1] - 2*v2]
                min_length = min(min_length, vector_length(v))
            return
        if count < half:
            dfs(idx + 1, count + 1, v1 + points[idx][0], v2 + points[idx][1])
        dfs(idx + 1, count, v1, v2)

    dfs(0, 0, 0, 0)
    return min_length

# 테스트 케이스 읽기
T = int(input())
for _ in range(T):
    N = int(input())
    points = [tuple(map(int, input().split())) for _ in range(N)]
    print("{:.6f}".format(solve(points)))
