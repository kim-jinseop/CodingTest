from sys import stdin

n,m,k = map(int,stdin.readline().split())
board = stdin.read().split('\n')
ans = 4000000

sum_board = [[0] * (m+1) for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,m+1) :
        sum_board[i][j] = sum_board[i-1][j] + sum_board[i][j-1] - sum_board[i-1][j-1] + (((i+j)%2!=0 and board[i-1][j-1] == 'B') or ((i + j)%2==0 and board[i-1][j-1] == 'W'))

for i in range(0, n-k+1) :
    for j in range(0, m-k+1) :
        save = sum_board[i+k][j+k] - sum_board[i][j+k] - sum_board[i+k][j] + sum_board[i][j]
        ans = min(ans, min(save, k*k-save))

print(ans)