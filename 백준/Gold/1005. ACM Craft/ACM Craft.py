from collections import deque
import sys

def find_min_time(build_times, rules, target):
    n = len(build_times)
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    dp = [0] * (n + 1)

    for x, y in rules:
        graph[x].append(y)
        indegree[y] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = build_times[i - 1]

    while q:
        current = q.popleft()
        for next_node in graph[current]:
            indegree[next_node] -= 1
            dp[next_node] = max(dp[next_node], dp[current] + build_times[next_node - 1])
            if indegree[next_node] == 0:
                q.append(next_node)

    return dp[target]

def main():
    input_data = sys.stdin.readlines()
    idx = 0
    t = int(input_data[idx].strip())  # 첫 줄에 테스트 케이스의 수
    idx += 1

    for _ in range(t):
        n, k = map(int, input_data[idx].split())
        idx += 1
        build_times = list(map(int, input_data[idx].split()))
        idx += 1

        rules = []
        for _ in range(k):
            x, y = map(int, input_data[idx].split())
            rules.append((x, y))
            idx += 1

        target = int(input_data[idx].strip())
        idx += 1

        print(find_min_time(build_times, rules, target))

if __name__ == "__main__":
    main()
