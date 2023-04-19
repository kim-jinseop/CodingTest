from sys import stdin

INF = int(1e9)
n = int(stdin.readline())
rgb = [list(map(int,stdin.readline().split())) for _ in range(n)]
result = INF

for start in range(3) :
    dp = [[INF,INF,INF] for _ in range(n)]
    dp[0][start] = rgb[0][start] 

    for i in range(1,n) :
        dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])

    for end in range(3) :
        if start != end :
            result = min(result,dp[n-1][end])

print(result)