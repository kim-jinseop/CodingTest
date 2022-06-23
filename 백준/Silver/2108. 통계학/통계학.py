import sys
from collections import Counter
In = sys.stdin.readline

n = int(In())

data = []
for _ in range(n):
    data.append(int(In()))

data.sort()

# 산술 평균
q1 = round(sum(data)/n)
print(q1)

# 중앙 값
q2 = data[n//2]
print(q2)

# 최빈값
q3_data = Counter(data).most_common()
if len(q3_data) > 1 :
    if q3_data[0][1] == q3_data[1][1] :
        q3 = q3_data[1][0]
    else : 
        q3 = q3_data[0][0]
else :
    q3 = q3_data[0][0]
print(q3)

# 범위
q4 = max(data) - min(data)
print(q4)