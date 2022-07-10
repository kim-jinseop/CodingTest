from sys import stdin

n = stdin.readline().rstrip()

box = [0] * 10
for i in n :
    box[int(i)] += 1

cnt69 = int((box.pop(9)+box.pop(6)) / 2 + 0.5)
cnt = max(box)

cnt = max(cnt, cnt69)
print(cnt)
