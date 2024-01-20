import math

def calculate_positions(x1, y1, r1, x2, y2, r2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if distance == 0 and r1 == r2:
        return -1  # 두 원이 일치
    elif distance > r1 + r2 or distance < abs(r1 - r2):
        return 0  # 두 원이 만나지 않음
    elif distance == r1 + r2 or distance == abs(r1 - r2):
        return 1  # 한 점에서 만남
    else:
        return 2  # 두 점에서 만남

# 입력 처리
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    print(calculate_positions(x1, y1, r1, x2, y2, r2))
