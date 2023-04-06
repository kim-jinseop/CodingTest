from sys import stdin

n = int(stdin.readline())
p = [0] + list(map(int,stdin.readline().split()))

dp = [0 for _ in range(n+1)]
for i in range(1,len(p)) :
    dp[i] = p[i]

for i in range(n+1) :
    for j in range(i) :
        dp[i] = max(dp[i-j]+dp[j], dp[i])


print(dp[-1])