from sys import stdin
from collections import deque

S = stdin.readline().rstrip()
T = stdin.readline().rstrip()
q = deque()
q.append(S)


while q :
    x = q.popleft()

    # 같은 문자일때
    if x==T :
        answer = 1
        break

    # 같은 문자를 못 찾았을 때
    if (len(x) >= len(T)) or ((x not in T) and (x[::-1] not in T)):
        continue

    q.append(x + "A")
    q.append((x + "B")[::-1])
else :
    answer = 0

print(answer)