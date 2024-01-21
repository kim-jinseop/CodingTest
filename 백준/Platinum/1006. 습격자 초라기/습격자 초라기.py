def solve(i):
  DP = [[2*N]*(N+1) for i in range(4)]; DP[i][-1] = 0
  for n in range(N):
    for i in range(4):
      DP[0][n] = min(DP[0][n],DP[i][n-1]+int(i&1==0)+int(i&2==0))
    if enemy[0][n]+enemy[1][n]<=M:
      DP[0][n] = min(DP[0][n],DP[0][n-1]+1)
    if enemy[0][n]+enemy[0][n+1]<=M:
      DP[1][n] = min(DP[0][n-1]+2,DP[2][n-1]+1)
    if enemy[1][n]+enemy[1][n+1]<=M:
      DP[2][n] = min(DP[0][n-1]+2,DP[1][n-1]+1)
    if enemy[0][n]+enemy[0][n+1]<=M and enemy[1][n]+enemy[1][n+1]<=M:
      DP[3][n] = DP[0][n-1]+2
  return DP

for _ in range(int(input())):
  N,M = map(int,input().split())
  enemy = [[*map(int,input().split()),0] for i in range(2)]
  result = solve(0)[0][N-1]
  if enemy[0][0]+enemy[0][N-1]<=M:
    DP = solve(1)
    result = min(result,DP[2][N-2]+1,DP[0][N-2]+2)
  if enemy[1][0]+enemy[1][N-1]<=M:
    DP = solve(2)
    result = min(result,DP[1][N-2]+1,DP[0][N-2]+2)
  if enemy[0][0]+enemy[0][N-1]<=M and enemy[1][0]+enemy[1][N-1]<=M:
    result = min(result,solve(3)[0][N-2]+2)
  print(result)