n = int(input())

box = [0] * 10001
box[1] = 1

for i in range(2,10001):
    box[i] = box[i-2] + box[i-1]

print(box[n])