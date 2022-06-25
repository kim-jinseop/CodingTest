import sys

In = sys.stdin.readline

n,m = map(int,In().split())

s = []
for _ in range(n) :
    s.append(In().rstrip())
s_set = set(s)

data = []
for _ in range(m) :
    data.append(In().rstrip())

count = 0
for i in data :
    if i in s_set :
        count += 1

print(count)