import sys
import itertools

inp = sys.stdin.readline
n = int(inp())
Min = int(1e9)
arr = []
for _ in range(n) :
    arr.append(list(map(int,inp().split())))

num = [i for i in range(n)]
num_pmt = list(itertools.combinations(num,n//2))

def ability(part) :
    team_s = list(itertools.permutations(part,2))
    team_l = list(itertools.permutations(set(num)-set(part),2))

    team_s_sum = 0 
    team_l_sum = 0

    for i in range(len(team_s)) :
        team_s_sum += arr[team_s[i][0]][team_s[i][1]]
        team_l_sum += arr[team_l[i][0]][team_l[i][1]]

    return abs(team_s_sum - team_l_sum)

for num_pmt_part in num_pmt :
    Min = min(Min,ability(num_pmt_part))

print(Min)
    